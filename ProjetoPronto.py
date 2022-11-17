from random import *
from time import time
import sys
sys.setrecursionlimit(2100000000)
#sys.setrecursionlimit(limit)
#import os

class Main:

    @staticmethod
    def main():
        opcao = "1"
        while opcao != "0":
            print(
                "\nPara quantos elementos voce deseja fazer o benchmark?\n1- 100 (Cem)\n2- 1000 (Mil)\n3- 10000 (Dez mil)\n4- 100000 (Cem mil)\n5- 1000000 (Um millh?o)\n0- Sair")
            opcao = input()
            if opcao == "1":
                Main.testeCemElementos()
            elif opcao == "2":
                Main.testeMilElementos()
            elif opcao == "3":
                Main.testeDezMilElementos()
            elif opcao == "4":
                Main.testeCemMilElementos()
            elif opcao == "5":
                Main.testeUmMilhaoElementos()
            elif opcao == "0":
                print("FIM!")
            else:
                print("Opção Invalida!, Tente denovo!")

    @staticmethod
    def partition(a, start, end):
        pivot = a[end]
        i = (start - 1)
        j = start
        while float(j) <= float(end - 1):
            if a[j] < pivot:
                i += 1
                t = a[i]
                a[i] = a[j]
                a[j] = t
            j += 1
        t = a[i + 1]
        a[i + 1] = a[end]
        a[end] = t
        return i + 1

    # Quick Sort
    @staticmethod
    def quickSort(a, start, end):
        comeco = int(time() * 1000)
        try:
            if start < end:
                p = Main.partition(a, start, end)
                Main.quickSort(a, start, p - 1)
                Main.quickSort(a, p + 1, end)
        except MemoryError:
            tempo = int(time() * 1000) - comeco
            return tempo
        tempo = int(time() * 1000) - comeco
        return tempo

    @staticmethod
    def merge(a, beg, mid, end):
        i = 0
        j = 0
        k = 0
        n1 = mid - beg + 1
        n2 = end - mid
        LeftArray = [0] * n1
        RightArray = [0] * n2
        i = 0
        while i < n1:
            LeftArray[i] = a[beg + i]
            i += 1
        j = 0
        while j < n2:
            RightArray[j] = a[mid + 1 + j]
            j += 1
        i = 0
        j = 0
        k = beg
        while i < n1 and j < n2:
            if LeftArray[i] <= RightArray[j]:
                a[k] = LeftArray[i]
                i += 1
            else:
                a[k] = RightArray[j]
                j += 1
            k += 1
        while i < n1:
            a[k] = LeftArray[i]
            i += 1
            k += 1
        while j < n2:
            a[k] = RightArray[j]
            j += 1
            k += 1

    # Merge Sort
    @staticmethod
    def mergeSort(a, beg, end):
        comeco = int(time() * 1000)
        if beg < end:
            mid = int((beg + end) / 2)
            Main.mergeSort(a, beg, mid)
            Main.mergeSort(a, mid + 1, end)
            Main.merge(a, beg, mid, end)
        tempo = int(time() * 1000) - comeco
        return tempo

    # Shell Sort
    @staticmethod
    def shellSort(arr):
        comeco = int(time() * 1000)
        n = len(arr)
        gap = int(n / 2)
        while gap > 0:
            i = gap
            while i < n:
                key = arr[int(i)]
                j = i
                while j >= gap and arr[int(j) - int(gap)] > key:
                    arr[int(j)] = arr[int(j) - int(gap)]
                    j -= gap
                arr[int(j)] = key
                i += 1
            gap /= 2
        tempo = int(time() * 1000) - comeco
        return tempo

    # Bubble Sort
    @staticmethod
    def bubbleSort(arr):
        comeco = int(time() * 1000)
        n = len(arr)
        temp = 0
        i = 0
        while i < n:
            j = 1
            while j < (n - i):
                if arr[j - 1] > arr[j]:
                    temp = arr[j - 1]
                    arr[j - 1] = arr[j]
                    arr[j] = temp
                j += 1
            i += 1
        tempo = int(time() * 1000) - comeco
        return tempo

    # Selection Sort
    @staticmethod
    def selectionSort(arr):
        comeco = int(time() * 1000)
        i = 0
        while i < len(arr) - 1:
            index = i
            j = i + 1
            while j < len(arr):
                if arr[j] < arr[index]:
                    index = j
                j += 1
            smallerNumber = arr[index]
            arr[index] = arr[i]
            arr[i] = smallerNumber
            i += 1
        tempo = int(time() * 1000) - comeco
        return tempo

    # Insertion Sort
    @staticmethod
    def insertionSort(array):
        comeco = int(time() * 1000)
        i = 0
        while i < len(array):
            j = i
            while j > 0 and array[j - 1] > array[j]:
                key = array[j]
                array[j] = array[j - 1]
                array[j - 1] = key
                j = j - 1
            i += 1
        tempo = int(time() * 1000) - comeco
        return tempo

    # Gerar aleatorios, crescentes e decrescentes
    @staticmethod
    def gerarNumeros():
        aux = 1000001
        i = 0
        while i < 1000000:
            if i < 100:
                Main.vetor100aleatorio[i] = 1 + int((random()  *  100))
                Main.vetor100crescente[i] = i
                Main.vetor100decrescente[i] = aux - 1
            if i < 1000:
                Main.vetor1000aleatorio[i] = 1 + int((random() * 1000))
                Main.vetor1000crescente[i] = i
                Main.vetor1000decrescente[i] = aux - 1
            if i < 10000:
                Main.vetor10000aleatorio[i] = 1 + int((random() * 10000))
                Main.vetor10000crescente[i] = i
                Main.vetor10000decrescente[i] = aux - 1
            if i < 100000:
                Main.vetor100000aleatorio[i] = 1 + int((random() * 100000))
                Main.vetor100000crescente[i] = i
                Main.vetor100000decrescente[i] = aux - 1
            if i < 1000000:
                Main.vetor1000000aleatorio[i] = 1 + int((random() * 1000000))
                Main.vetor1000000crescente[i] = i
                Main.vetor1000000decrescente[i] = aux - 1
            aux -= 1
            i += 1

    @staticmethod
    def testeCemElementos():
        Main.gerarNumeros()
        print("Tempo Insertion Sort (numeros aleatorios): " + str(
            Main.insertionSort(Main.vetor100aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros aleatorios): " + str(
            Main.selectionSort(Main.vetor100aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print(
            "Tempo Bubble Sort (numeros aleatorios): " + str(Main.bubbleSort(Main.vetor100aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros aleatorios): " + str(Main.shellSort(Main.vetor100aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros aleatorios): " + str(
            Main.mergeSort(Main.vetor100aleatorio, 0, len(Main.vetor100aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros aleatorios): " + str(
            Main.quickSort(Main.vetor100aleatorio, 0, len(Main.vetor100aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros crescentes): " + str(
            Main.insertionSort(Main.vetor100crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros crescentes): " + str(
            Main.selectionSort(Main.vetor100crescente)) + " milisegundos")
        Main.gerarNumeros()
        print(
            "Tempo Bubble Sort (numeros crescentes): " + str(Main.bubbleSort(Main.vetor100crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros crescentes): " + str(Main.shellSort(Main.vetor100crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros crescentes): " + str(
            Main.mergeSort(Main.vetor100crescente, 0, len(Main.vetor100crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros crescentes): " + str(
            Main.quickSort(Main.vetor100crescente, 0, len(Main.vetor100crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros decrescentes): " + str(
            Main.insertionSort(Main.vetor100decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros decrescentes): " + str(
            Main.selectionSort(Main.vetor100decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros decrescentes): " + str(
            Main.bubbleSort(Main.vetor100decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros decrescentes): " + str(
            Main.shellSort(Main.vetor100decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros decrescentes): " + str(
            Main.mergeSort(Main.vetor100decrescente, 0, len(Main.vetor100decrescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros decrescentes): " + str(
            Main.quickSort(Main.vetor100decrescente, 0, len(Main.vetor100decrescente) - 1)) + " milisegundos")

    @staticmethod
    def testeMilElementos():
        Main.gerarNumeros()
        print("Tempo Insertion Sort (numeros aleatorios): " + str(
            Main.insertionSort(Main.vetor1000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros aleatorios): " + str(
            Main.selectionSort(Main.vetor1000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros aleatorios): " + str(
            Main.bubbleSort(Main.vetor1000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print(
            "Tempo Shell Sort (numeros aleatorios): " + str(Main.shellSort(Main.vetor1000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros aleatorios): " + str(
            Main.mergeSort(Main.vetor1000aleatorio, 0, len(Main.vetor1000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros aleatorios): " + str(
            Main.quickSort(Main.vetor1000aleatorio, 0, len(Main.vetor1000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros crescentes): " + str(
            Main.insertionSort(Main.vetor1000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros crescentes): " + str(
            Main.selectionSort(Main.vetor1000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros crescentes): " + str(
            Main.bubbleSort(Main.vetor1000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print(
            "Tempo Shell Sort (numeros crescentes): " + str(Main.shellSort(Main.vetor1000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros crescentes): " + str(
            Main.mergeSort(Main.vetor1000crescente, 0, len(Main.vetor1000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros crescentes): " + str(
            Main.quickSort(Main.vetor1000crescente, 0, len(Main.vetor1000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros decrescentes): " + str(
            Main.insertionSort(Main.vetor1000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros decrescentes): " + str(
            Main.selectionSort(Main.vetor1000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros decrescentes): " + str(
            Main.bubbleSort(Main.vetor1000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros decrescentes): " + str(
            Main.shellSort(Main.vetor1000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros decrescentes): " + str(
            Main.mergeSort(Main.vetor1000decrescente, 0, len(Main.vetor1000decrescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros decrescentes): " + str(
            Main.quickSort(Main.vetor1000decrescente, 0, len(Main.vetor1000decrescente) - 1)) + " milisegundos")

    @staticmethod
    def testeDezMilElementos():
        Main.gerarNumeros()
        print("Tempo Insertion Sort (numeros aleatorios): " + str(
            Main.insertionSort(Main.vetor10000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros aleatorios): " + str(
            Main.selectionSort(Main.vetor10000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros aleatorios): " + str(
            Main.bubbleSort(Main.vetor10000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print(
            "Tempo Shell Sort (numeros aleatorios): " + str(Main.shellSort(Main.vetor10000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros aleatorios): " + str(
            Main.mergeSort(Main.vetor10000aleatorio, 0, len(Main.vetor10000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros aleatorios): " + str(
            Main.quickSort(Main.vetor10000aleatorio, 0, len(Main.vetor10000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros crescentes): " + str(
            Main.insertionSort(Main.vetor10000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros crescentes): " + str(
            Main.selectionSort(Main.vetor10000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros crescentes): " + str(
            Main.bubbleSort(Main.vetor10000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print(
            "Tempo Shell Sort (numeros crescentes): " + str(Main.shellSort(Main.vetor10000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros crescentes): " + str(
            Main.mergeSort(Main.vetor10000crescente, 0, len(Main.vetor10000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros crescentes): " + str(
            Main.quickSort(Main.vetor10000crescente, 0, len(Main.vetor10000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros decrescentes): " + str(
            Main.insertionSort(Main.vetor10000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros decrescentes): " + str(
            Main.selectionSort(Main.vetor10000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros decrescentes): " + str(
            Main.bubbleSort(Main.vetor10000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros decrescentes): " + str(
            Main.shellSort(Main.vetor10000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros decrescentes): " + str(
            Main.mergeSort(Main.vetor10000decrescente, 0, len(Main.vetor10000decrescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros decrescentes): " + str(
            Main.quickSort(Main.vetor10000decrescente, 0, len(Main.vetor10000decrescente) - 1)) + " milisegundos")

    @staticmethod
    def testeCemMilElementos():
        Main.gerarNumeros()
        print("Tempo Insertion Sort (numeros aleatorios): " + str(
            Main.insertionSort(Main.vetor100000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros aleatorios): " + str(
            Main.selectionSort(Main.vetor100000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros aleatorios): " + str(
            Main.bubbleSort(Main.vetor100000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros aleatorios): " + str(
            Main.shellSort(Main.vetor100000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros aleatorios): " + str(
            Main.mergeSort(Main.vetor100000aleatorio, 0, len(Main.vetor100000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros aleatorios): " + str(
            Main.quickSort(Main.vetor100000aleatorio, 0, len(Main.vetor100000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros crescentes): " + str(
            Main.insertionSort(Main.vetor100000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros crescentes): " + str(
            Main.selectionSort(Main.vetor100000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros crescentes): " + str(
            Main.bubbleSort(Main.vetor100000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros crescentes): " + str(
            Main.shellSort(Main.vetor100000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros crescentes): " + str(
            Main.mergeSort(Main.vetor100000crescente, 0, len(Main.vetor100000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros crescentes): " + str(
            Main.quickSort(Main.vetor100000crescente, 0, len(Main.vetor100000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros decrescentes): " + str(
            Main.insertionSort(Main.vetor100000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros decrescentes): " + str(
            Main.selectionSort(Main.vetor100000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros decrescentes): " + str(
            Main.bubbleSort(Main.vetor100000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros decrescentes): " + str(
            Main.shellSort(Main.vetor100000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros decrescentes): " + str(
            Main.mergeSort(Main.vetor100000decrescente, 0, len(Main.vetor100000decrescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros decrescentes): " + str(
            Main.quickSort(Main.vetor100000decrescente, 0, len(Main.vetor100000decrescente) - 1)) + " milisegundos")

    @staticmethod
    def testeUmMilhaoElementos():
        Main.gerarNumeros()
        print("Tempo Insertion Sort (numeros aleatorios): " + str(
            Main.insertionSort(Main.vetor1000000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros aleatorios): " + str(
            Main.selectionSort(Main.vetor1000000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros aleatorios): " + str(
            Main.bubbleSort(Main.vetor1000000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros aleatorios): " + str(
            Main.shellSort(Main.vetor1000000aleatorio)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros aleatorios): " + str(
            Main.mergeSort(Main.vetor1000000aleatorio, 0, len(Main.vetor1000000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros aleatorios): " + str(
            Main.quickSort(Main.vetor1000000aleatorio, 0, len(Main.vetor1000000aleatorio) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros crescentes): " + str(
            Main.insertionSort(Main.vetor1000000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros crescentes): " + str(
            Main.selectionSort(Main.vetor1000000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros crescentes): " + str(
            Main.bubbleSort(Main.vetor1000000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros crescentes): " + str(
            Main.shellSort(Main.vetor1000000crescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros crescentes): " + str(
            Main.mergeSort(Main.vetor1000000crescente, 0, len(Main.vetor1000000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros crescentes): " + str(
            Main.quickSort(Main.vetor1000000crescente, 0, len(Main.vetor1000000crescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("\nTempo Insertion Sort (numeros decrescentes): " + str(
            Main.insertionSort(Main.vetor1000000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Selection Sort (numeros decrescentes): " + str(
            Main.selectionSort(Main.vetor1000000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Bubble Sort (numeros decrescentes): " + str(
            Main.bubbleSort(Main.vetor1000000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Shell Sort (numeros decrescentes): " + str(
            Main.shellSort(Main.vetor1000000decrescente)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Merge Sort (numeros decrescentes): " + str(
            Main.mergeSort(Main.vetor1000000decrescente, 0, len(Main.vetor1000000decrescente) - 1)) + " milisegundos")
        Main.gerarNumeros()
        print("Tempo Quick Sort (numeros decrescentes): " + str(
            Main.quickSort(Main.vetor1000000decrescente, 0, len(Main.vetor1000000decrescente) - 1)) + " milisegundos")

    vetor100aleatorio = [0] * 100
    vetor100crescente = [0] * 100
    vetor100decrescente = [0] * 100
    vetor1000aleatorio = [0] * 1000
    vetor1000crescente = [0] * 1000
    vetor1000decrescente = [0] * 1000
    vetor10000aleatorio = [0] * 10000
    vetor10000crescente = [0] * 10000
    vetor10000decrescente = [0] * 10000
    vetor100000aleatorio = [0] * 100000
    vetor100000crescente = [0] * 100000
    vetor100000decrescente = [0] * 100000
    vetor1000000aleatorio = [0] * 1000000
    vetor1000000crescente = [0] * 1000000
    vetor1000000decrescente = [0] * 1000000

if __name__ == "__main__":
    Main.main()
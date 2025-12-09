"""Exerc ́ıcio: 1.
Implemente os seguintes algoritmos de ordena ̧c ̃ao e modifique-os para imprimir a quantidade
de testes e trocas efetuadas durante a ordena ̧c ̃ao.
 Insertion Sort.
 Selection Sort.
 Bubble Sort.
 Shell Sort.
 Merge Sort.
 Quick Sort.
 Heap Sort.
 Counting Sort.
Lista de Testes
 12 42 83 25 67 71 3 4 94 53
 100 48 19 61 86 33 13 43 84 28
 81 60 6 49 40 41 38 64 44 36
 45 27 11 89 63 39 9 58 52 17
 88 77 26 62 30 96 56 65 98 99
 76 73 16 95 35 87 68 69 51 92
 37 75 90 82 8 18 23 93 57 10
 15 97 14 29 7 24 31 59 78 85
 5 70 55 91 47 72 2 20 34 74
 50 66 32 22 54 79 21 1 80 46"""


# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    comparisons = 0  # Testes
    swaps = 0        # Trocas

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Comparações (Testes)
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                # Trocas
                arr[j + 1] = arr[j]
                j -= 1
                swaps += 1 # Contamos o "shift" como uma troca ou movimento
            else:
                break
        
        # A posição final para a 'key' é j + 1
        if arr[j + 1] != key:
             arr[j + 1] = key
             swaps += 1 # Contamos a inserção final como uma troca/movimento
    
    return arr, comparisons, swaps

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    comparisons = 0  # Testes
    swaps = 0        # Trocas

    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            comparisons += 1  # Comparações (Testes)
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Troca o elemento encontrado pelo primeiro elemento não ordenado
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            
    return arr, comparisons, swaps

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0  # Testes
    swaps = 0        # Trocas

    for i in range(n - 1):
        # O último 'i' elementos já estão no lugar
        for j in range(0, n - i - 1):
            comparisons += 1  # Comparações (Testes)
            if arr[j] > arr[j + 1]:
                # Trocas
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                
    return arr, comparisons, swaps

# Shell Sort
def shell_sort(arr):
    n = len(arr)
    comparisons = 0  # Testes
    swaps = 0        # Trocas
    gap = n // 2

    # Inicia com o maior gap e o reduz
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Insertion Sort com o gap atual
            while j >= gap:
                comparisons += 1 # Comparações (Testes)
                if arr[j - gap] > temp:
                    # Trocas
                    arr[j] = arr[j - gap]
                    j -= gap
                    swaps += 1 # Contamos o 'shift' como uma troca/movimento
                else:
                    break
            
            if arr[j] != temp:
                 arr[j] = temp
                 swaps += 1 # Contamos a inserção final como uma troca/movimento
        
        gap //= 2
        
    return arr, comparisons, swaps

# Merge Sort
def merge_sort_count(arr):
    comparisons = 0
    swaps = 0 
    
    # Função auxiliar para a intercalação (merge)
    def merge(arr, l, m, r):
        nonlocal comparisons, swaps
        
        n1 = m - l + 1
        n2 = r - m
    
        L = [0] * n1
        R = [0] * n2
    
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        i = 0     
        j = 0     
        k = l     
    
        while i < n1 and j < n2:
            comparisons += 1 # Comparações (Testes)
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
                swaps += 1 # Contamos o movimento como uma troca/movimento
            else:
                arr[k] = R[j]
                j += 1
                swaps += 1 # Contamos o movimento como uma troca/movimento
            k += 1
    
        # Copia os elementos restantes de L[]
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            swaps += 1 
    
        # Copia os elementos restantes de R[]
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            swaps += 1
            
    # Função principal de ordenação recursiva
    def merge_sort_recursive(arr, l, r):
        if l < r:
            m = l + (r - l) // 2
    
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m + 1, r)
            merge(arr, l, m, r)

    arr_copy = arr[:] # Faz uma cópia para ordenar
    merge_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    
    return arr_copy, comparisons, swaps

# Quick Sort
def quick_sort_count(arr):
    comparisons = 0
    swaps = 0

    # Função que particiona o array e retorna o índice do pivô
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1  # Índice do elemento menor
        
        for j in range(low, high):
            comparisons += 1 # Comparações (Testes)
            if arr[j] <= pivot:
                i = i + 1
                # Trocas
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        # Troca o pivô com o elemento na posição i+1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    # Função principal de ordenação recursiva
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    arr_copy = arr[:] # Faz uma cópia para ordenar
    quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    
    return arr_copy, comparisons, swaps

# Heap Sort
def heap_sort_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    def heapify(arr, n, i):
        nonlocal comparisons, swaps
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # Verifica se o filho esquerdo existe e é maior que a raiz
        if l < n:
            comparisons += 1 # Comparações (Testes)
            if arr[l] > arr[largest]:
                largest = l

        # Verifica se o filho direito existe e é maior que o maior até agora
        if r < n:
            comparisons += 1 # Comparações (Testes)
            if arr[r] > arr[largest]:
                largest = r

        # Se o maior não for a raiz
        if largest != i:
            # Trocas
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps += 1
            # Chama heapify na subárvore afetada
            heapify(arr, n, largest)

    arr_copy = arr[:]
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copy, n, i)

    # 2. Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
        swaps += 1
        heapify(arr_copy, i, 0)
        
    return arr_copy, comparisons, swaps

# Counting Sort
def counting_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    max_val = max(arr) 

    # 1. Cria o array de contagem (do tamanho max_val + 1)
    count = [0] * (max_val + 1)
    # 2. Armazena a contagem de cada caractere
    for num in arr:
        count[num] += 1  
    # 3. Altera count[i] para conter a posição de saída
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # 4. Constrói o array de saída
    output = [0] * n
    for num in reversed(arr):
        # O elemento é movido para o array de saída:
        output[count[num] - 1] = num
        count[num] -= 1
        swaps += 1 # Contamos o movimento para o array de saída como uma 'troca'
    # Copia o array de saída para arr original
    for i in range(n):
        arr[i] = output[i]
        
    return arr, comparisons, swaps


if __name__ == "__main__":
    test_arrays = [
        [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
        [100, 48, 19, 61, 86, 33, 13, 43, 84, 28],
        [81, 60, 6, 49, 40, 41, 38, 64, 44, 36],
        [45, 27, 11, 89, 63, 39, 9, 58, 52, 17],
        [88, 77, 26, 62, 30, 96, 56, 65, 98, 99],
        [76, 73, 16, 95, 35, 87, 68, 69, 51, 92],
        [37, 75, 90, 82, 8, 18, 23, 93, 57, 10],
        [15, 97, 14, 29, 7, 24, 31, 59, 78, 85],
        [5, 70, 55, 91, 47, 72, 2, 20, 34, 74],
        [50, 66, 32, 22, 54, 79, 21, 1, 80, 46]
    ]
    
    print("=" * 50)
    print(f"Lista Original de Teste: {test_arrays}")
    print("=" * 50)

    # 1. Insertion Sort
    arr_is = test_arrays[0][:] # Copia a lista
    sorted_is, comp_is, swap_is = insertion_sort(arr_is)
    print(f"**1. Insertion Sort**")
    print(f"Ordenada: {sorted_is}")
    print(f"Testes (Comparações): {comp_is}, Trocas (Movimentos): {swap_is}")
    print("-" * 50)

    # 2. Selection Sort
    arr_ss = test_arrays[1][:]
    sorted_ss, comp_ss, swap_ss = selection_sort(arr_ss)
    print(f"**2. Selection Sort**")
    print(f"Ordenada: {sorted_ss}")
    print(f"Testes (Comparações): {comp_ss}, Trocas (Swaps): {swap_ss}")
    print("-" * 50)

    # 3. Bubble Sort
    arr_bs = test_arrays[2][:]
    sorted_bs, comp_bs, swap_bs = bubble_sort(arr_bs)
    print(f"**3. Bubble Sort**")
    print(f"Ordenada: {sorted_bs}")
    print(f"Testes (Comparações): {comp_bs}, Trocas (Swaps): {swap_bs}")
    print("-" * 50)

    # 4. Shell Sort
    arr_shs = test_arrays[3][:]
    sorted_shs, comp_shs, swap_shs = shell_sort(arr_shs)
    print(f"**4. Shell Sort**")
    print(f"Ordenada: {sorted_shs}")
    print(f"Testes (Comparações): {comp_shs}, Trocas (Movimentos): {swap_shs}")
    print("-" * 50)
    
    # 5. Merge Sort
    sorted_ms, comp_ms, swap_ms = merge_sort_count(test_arrays[4])
    print(f"**5. Merge Sort**")
    print(f"Ordenada: {sorted_ms}")
    print(f"Testes (Comparações): {comp_ms}, Trocas (Movimentos): {swap_ms}")
    print("-" * 50)
    
    # 6. Quick Sort
    sorted_qs, comp_qs, swap_qs = quick_sort_count(test_arrays[5])
    print(f"**6. Quick Sort**")
    print(f"Ordenada: {sorted_qs}")
    print(f"Testes (Comparações): {comp_qs}, Trocas (Swaps): {swap_qs}")
    print("-" * 50)
    
    # 7. Heap Sort
    sorted_hs, comp_hs, swap_hs = heap_sort_count(test_arrays[6])
    print(f"**7. Heap Sort**")
    print(f"Ordenada: {sorted_hs}")
    print(f"Testes (Comparações): {comp_hs}, Trocas (Swaps): {swap_hs}")
    print("-" * 50)

    # 8. Counting Sort
    arr_cs = test_arrays[7][:]
    sorted_cs, comp_cs, swap_cs = counting_sort(arr_cs)
    print(f"**8. Counting Sort**")
    print(f"Ordenada: {sorted_cs}")
    print(f"Testes (Comparações): {comp_cs}, Trocas (Movimentos): {swap_cs}")
    print("=" * 50)
import heapq
from collections import Counter, deque
from memory_profiler import profile
import timeit

@profile
def huffman_1():
    def huffman_encode(frequency):
        heap = [[wt, [sym, ""]] for sym, wt in frequency.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    txt = input('Введите текст для кодирования: ')
    if len(txt) > 1:
        freq = Counter()
        for ch in txt:
            freq[ch] += 1

        huff = huffman_encode(freq)

        print("Символ\t\tЧастота\t\tКод Хаффмана")
        for ch in huff:
            print(ch[0], "\t\t\t", freq[ch[0]], "\t\t\t", ch[1])

     encode = ''.join(el[1] for ch in txt for el in huff if ch == el[0])
        print(f'Закодированная строка: {encode}')
    else:
        print('Нечего кодировать.')
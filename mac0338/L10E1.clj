(defn subseq?
  [A n B k]
  (if (or (neg? n) (neg? k))
    (neg? k)
    (if (= (nth A n) (nth B k))
      (subseq? A (dec n) B (dec k))
      (subseq? A (dec n) B k))))

(def A [1 2 3 4 5 6 7 8 9])
(def B [7 8 9])

(println (subseq? A (dec (count A)) B (dec (count B))))


; É-SUBSEQ(A, n, B, k)
; 1    se n = 0 e k = 0
; 2        se k = 0 devolva Sim
; 3        senão devolva Não
; 4    se A[n] = B[k]
; 5      devolva É-SUBSEQ(A, n-1, B, k-1)
; 6    senão devolva É-SUBSEQ(A, n-1, B, k)


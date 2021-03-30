(defn maximo
  [a p r]
  (if (= p r)
    (nth a p)
    (let [q (quot (+ p r) 2)
          max-esq (maximo a p q)
          max-dir (maximo a (+ q 1) r)]
      (if (> max-esq max-dir)
        max-esq
        max-dir))))

; idx = 0 1 2 3 4 5 6 7 8
(def a [2 9 3 4 8 1 5 6 7])
(def p 0)
(def r 3)

(println (maximo a p r))



; MAXIMO (A, p, r): 
;    se p = r                      1
;        devolva A[p]              1
;    q := piso((p+r)/2)            1
;    max_esq := MAXIMO (A, p, q)   
;    max_dir := MAXIMO (A, q+1, r) 
;    se max_esq > max_dir          1
;        devolva max_esq           1
;    senão devolva max_dir         1

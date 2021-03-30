(defn scd-max-guloso
  [a b k r]
  (loop [m (inc k)]
    (if (and (<= m r) (<= (nth a m) (nth b k)))
      (recur (inc m))
      (do
        (println "m é " m)
        (if (<= m r)
          (conj (scd-max-guloso a b m r) m)
          '())))))

(defn scd-max-r
  [a b p r]
  (let [ar (conj a 0)
        br (conj b 0)]
    (scd-max-guloso ar br (dec p) r)))

; idx 0  1  2  3  4  5  6  7  8
(def a '(6  9  7  18 1  23 25 30))
(def b '(15 15 16 24 26 28 30 34))

(def scd (scd-max-r a b 1 (count a)))

(println (sort a))

(println "\nmax scd indices: " scd)
(println "\nintervals: ")
(doseq [index scd]
  (let [idx (dec index)]
    (println idx ":" (nth a idx) ".." (nth b idx))))

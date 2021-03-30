const isSubseq1 = (A, n, B, k) => {
	let j = k-1;
	console.log('1')
	for (let i = n-1; i >= 0; i--) {
		console.error('i', i)
		console.error('j', j)
		console.error()
		if (A[i] == B[j]) {
			j--;
		}
	}

	return j < 0;
}

const isSubseq2 = (A, n, B, k) => {
	let i = n-1;
	let j = k-1;
	console.log('2')
	while (i >= 0 && j >= 0) {
		console.error('i', i)
		console.error('j', j)
		console.error()
		if (A[i] == B[j]) {
			j--;
		}
		i--;
	}

	return j < 0;
}

const A = [1, 2, 3, 4, 5, 6, 7, 8];
const B = [6, 7, 8];

console.log(isSubseq1(A, A.length, B, B.length));
console.log(isSubseq2(A, A.length, B, B.length));


// ; É-SUBSEQ(A, n, B, k)
// ; 1    j := k
// ; 2    i := n
// ; 3    enquanto i > 0 e j > 0
// ; 4        se A[i] = B[j]
// ; 5            j := j - 1
// ; 6        i := i - 1
// ; 7    se j = 0 devolva SIM
// ; 8    senão devolva NÃO
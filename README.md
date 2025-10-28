
420-SN1-RE: Programming in Science Fall 2025, Section 007 and Section 008  

# Programming in Science - Lab 8

This template repository is the starter project for **Programming in Science Lab 8**.  
Written in Python, and tested with **unittest**.

---

### Question(s)

1. **(50%)** Dot Product of Two Vectors:
   
   - Write a function `dot_product(A, B)` that computes and returns the **dot product** of two vectors.  
     The vectors `A` and `B` must have the same length.

   #### Mathematical Definition:
   $$
   \vec{A} \cdot \vec{B} = \sum_{i=1}^{n} (A_i \times B_i)
   $$
   #### Example:
   ```python
   dot_product([1, 2, 3], [4, 5, 6])  # Returns 32
````


✅ **Hints:**

* Multiply corresponding elements of both vectors.
* Use a loop or list comprehension to accumulate the sum.
* Ensure both vectors are of the same size before computing.

---


2. **(50%)** Determine Orthogonality:
   
   - Write a function `is_orthogonal(V, W)` that determines whether two vectors **V** and **W** are **perpendicular (orthogonal)** based on their dot product.
   - Use the principle that **two non-zero vectors are orthogonal if their dot product equals zero**.

   #### Example:
   ```python
   is_orthogonal([1, 2], [-2, 1])   # Returns True
   is_orthogonal([2, 3], [4, 5])    # Returns False


✅ **Hints:**

* Use your `dot_product()` function to compute the dot product of the two vectors.
* If the dot product equals 0, return `True`; otherwise, return `False`.
* Remember to verify that both vectors are **non-zero** before testing orthogonality.


### Run Command

To run the tests, use the following command in your terminal:

```bash
python -m unittest test_Lab9.py
```

---




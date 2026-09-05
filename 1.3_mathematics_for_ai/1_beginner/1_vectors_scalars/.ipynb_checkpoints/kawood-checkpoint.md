# Kawood Mastery Challenge — Vectors and Scalars

Understand the core mathematical objects of AI: scalars for magnitude and vectors for direction and data representation.

## Question 1: Scalar vs Vector Definition
In AI, what's the difference between a scalar (learning rate = 0.001) and a vector (prediction = [0.1, 0.2, 0.7])?
- B. Scalar is a single number; vector is an ordered collection of numbers—scalars represent single quantities; vectors represent multiple dimensions; neural networks transform vectors through layers- C. They're the same- D. Scalars are numbers; vectors are always in physics- A. AI only uses scalars
**Answer: B** — Scalars are 0D; vectors are 1D.

---

## Question 2: Vector Magnitude
A vector v = [3, 4]. What's its magnitude, and what does magnitude represent?
- A. Magnitude = √(3² + 4²) = 5—magnitude is vector length/norm, representing the distance from origin in vector space; used in normalization and regularization- D. Magnitude = 3 + 4 = 7- C. Vectors don't have magnitude- B. Magnitude is always 1
**Answer: A** — Magnitude is vector length.

---

## Question 3: Vector Normalization
A model outputs logits [2, 4, 1]. You normalize them to unit length. Why is normalization useful?
- B. Normalization makes vectors comparable regardless of magnitude—important for softmax (converts logits to probabilities), cosine similarity (compares directions, not magnitudes), and numerical stability- A. Normalization doesn't help- D. Only neural networks need it- C. It's just cosmetic
**Answer: B** — Normalization enables fair comparison and stability.

---

## Question 4: Vector Notation and Indexing
Vector v = [5, -2, 3]. What are v[0], v[1], v[2]?
- D. v[0] = 5 (first component), v[1] = -2 (second), v[2] = 3 (third)—vectors are indexed like arrays; in AI, each component often represents a feature or neuron activation- C. All indices have the same value- A. Indexing vectors is impossible- B. Vectors are atomic units
**Answer: D** — Vector components are indexed like arrays.

---

## Question 5: Vector Operations: Dot Product
Two vectors u = [1, 2] and v = [3, 4]. Compute their dot product (u · v).
- A. u · v = 1×3 + 2×4 = 11—dot product measures alignment; high dot product means vectors point similar directions; low means orthogonal; used in neural networks for neuron activations- D. u · v = 1 + 2 + 3 + 4 = 10- C. u · v = u[0] × v[1] + u[1] × v[0] = 4- B. Dot product isn't defined
**Answer: A** — Dot product measures alignment.

---

## Question 6: Vector Addition
In neural networks, why is vector addition central? (e.g., output = weight × input + bias)
- A. Vector addition combines contributions—weights transform input, bias shifts the result; in deep networks, vectors add layer-by-layer, enabling feature composition- C. Addition is just one operation- D. Networks don't use addition- B. Addition complicates networks
**Answer: A** — Addition combines separate contributions.

---

## Question 7: Coordinate Systems
A vector v = [3, 4] in 2D coordinates (x, y). If you change to new coordinates rotated 45°, does the vector itself change, or just its representation?
- D. Vector is unchanged (same object); representation changes—this is crucial in AI: embeddings are coordinate-free; only the coordinate system matters—transforming coordinates doesn't change meaning- A. Vector changes- C. Coordinates and vectors are the same- B. Rotation breaks vectors
**Answer: D** — Vectors are coordinate-independent; representations are not.

---

## Question 8: Vector Spaces in AI
An embedding space maps words to vectors. Why vector space? (Why not just list all words and their properties?)
- D. Vector spaces enable geometric operations—similarity is distance, analogies are vector arithmetic (king - man + woman ≈ queen); vector spaces make similarity and relationships learnable and computable- C. Lists are equivalent- B. Vector spaces are just convention- A. AI doesn't use vector spaces
**Answer: D** — Vector spaces enable geometric reasoning.

---

## Question 9: High-Dimensional Vectors
An image embedding is a vector in 2048-dimensional space. Can you visualize it? Why does this dimensionality matter in practice?
- A. You can't visualize 2048D directly, but you can project to 2D (t-SNE, UMAP) for visualization—high dimensionality is powerful (more features) but challenging (curse of dimensionality, computational cost, sparse data)- B. Visualize each dimension separately- C. High dimensions are impossible- D. Dimensionality doesn't matter
**Answer: A** — High-dimensional vectors are abstract yet powerful.

---

## Question 10: Orthogonal Vectors
Two vectors are orthogonal if their dot product is 0. Why is orthogonality useful in AI?
- A. Orthogonal vectors are independent—changes in one don't affect the other; in neural networks, orthogonal features don't compete; regularization (like spectral normalization) encourages orthogonality for stability- D. Orthogonal vectors are identical- B. Orthogonality is just mathematical curiosity- C. AI doesn't use orthogonality
**Answer: A** — Orthogonality represents independence.

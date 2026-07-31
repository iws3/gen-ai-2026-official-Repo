# NumPy Foundations: Vectors & Matrices Workout (GenAI Edition)

**For:** Seed AI Bootcampers heading into ML/DL/GenAI
**Goal:** Build real, hands-on fluency with `numpy` (and a bit of `matplotlib`) — the two libraries under the hood of every embedding, every attention score, and every transformer layer you'll touch soon. Every exercise below is framed around a real GenAI concept — **word embeddings, attention scores, RAG retrieval, and transformer layers** — so you're not just learning math, you're previewing exactly what's coming.

---

## How to use this sheet

1. Open a Jupyter notebook (recommended, so plots render inline) and start with:
```python
import numpy as np
import matplotlib.pyplot as plt
```
2. Do **not** just read the questions — type the code yourself, run it, and check your output/plot against your own reasoning before peeking at any hints.
3. For every question, try to predict *first on paper* (even roughly) what shape/value/plot you expect, **then** confirm with code.
4. Solutions are in the collapsed section at the bottom — resist opening them until you've genuinely tried.

---

## Section A — Scalars & Vectors (a.k.a. what an "embedding" actually is)

### Q1. Scalars vs. Vectors
Create the following in NumPy and print each one's **type**, **shape**, and **number of dimensions (`.ndim`)**:
- A scalar `temperature = 0.7` (this is literally the "temperature" setting you'll see in every LLM API)
- A scalar wrapped as a NumPy array: `np.array(0.7)`
- A tiny toy **word embedding** `king_embedding = np.array([0.21, -0.05, 0.88, 0.14])` (in a real model this would be 768, 1536, or more numbers — we're using 4 to keep it visual)

**Think about it:** Why does `np.array(0.7)` have `shape = ()` and not `shape = (1,)`? What does that tell you about how NumPy distinguishes a true scalar from a 1-element vector? This distinction matters a lot once you're debugging shape errors in a transformer.

**Reality check:** a single GPT-style token embedding is just a vector like `king_embedding` — except with hundreds or thousands of numbers instead of 4. Everything you do below on a 4-number toy vector, a real model does on a 768+ number vector, millions of times a second.

---

### Q2. Building an Embedding Table
An **embedding table** is just a matrix where each row is one token's vector. Build a tiny 5-token embedding table:
1. A vector of the integers 0 through 9 using `np.arange` (pretend these are 10 token IDs).
2. A vector of 5 evenly spaced numbers between 0 and 1 (inclusive) using `np.linspace`.
3. A vector of 6 zeros, then a vector of 6 ones (this is what `[PAD]` and masking vectors often look like).
4. A `(5, 4)` matrix of random numbers drawn from a standard normal distribution — this is **exactly** how a real embedding table is initialized before training: `np.random.randn(5, 4)`, i.e. 5 tokens, each with a 4-dimensional embedding.

Print each, along with its `dtype` and (for #4) its `.shape`.

---

## Section B — Vector Operations & Visualization (a.k.a. attention scores)

### Q3. Elementwise Operations
Given two toy embeddings:
```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
```
Compute, **without using a for-loop**:
- `a + b`, `a - b`, `a * b`, `a / b`
- `a ** 2`
- The elementwise result of `(a - b) ** 2`

**Reflect:** `(a - b) ** 2` is the building block of squared error / MSE loss. `a + b` is also literally how some models *combine* embeddings (e.g., adding a token embedding and a positional embedding in a transformer — a step called "positional encoding"). Which NumPy behavior (broadcasting or vectorization) is letting you do all this in one line instead of a loop?

---

### Q4. Dot Product = Attention Score
In a transformer, an **attention score** between two tokens is (at its core) the dot product between a "query" vector and a "key" vector. Given:
```python
query = np.array([3, 4])   # a toy "query" vector for the word "it"
key   = np.array([4, 3])   # a toy "key" vector for the word "dog"
```
1. Compute the dot product **manually** with a for-loop, then confirm it matches `query @ key` and `np.dot(query, key)`. This number, informally, is "how much should 'it' attend to 'dog'?"
2. **Plot both vectors as arrows from the origin** using `plt.quiver`, on the same axes, with equal axis limits (e.g. `plt.xlim(-1, 6)`, `plt.ylim(-1, 6)`, `plt.gca().set_aspect('equal')`) so the geometry isn't distorted.
3. Compute the angle θ between `query` and `key` using:

$$\cos(\theta) = \frac{query \cdot key}{\|query\| \|key\|}$$

(`np.linalg.norm` for magnitude, `np.arccos` + `np.degrees` for the angle.) Add the angle value as a text label on your plot.

**Why this matters:** the dot product IS the core operation of self-attention (the mechanism that makes transformers — and therefore GPT, Claude, and every modern LLM — work). It's also the core of cosine similarity, which you'll use constantly in RAG.

---

## Section C — Unit Vectors & Visualization (a.k.a. preparing embeddings for RAG)

### Q5. Normalizing an Embedding — Before & After
Given a toy document embedding `v = np.array([3, 4])`:

1. Compute its norm (magnitude) and the **unit vector** in the same direction (`v` divided by its own norm). Confirm the unit vector's norm is (very close to) `1.0`.
2. Write a reusable function — you will reuse this exact function in a RAG pipeline later:
```python
def normalize(vec):
    # your code here
    ...
```
3. **Plot `v` and its normalized version on the same axes** as two arrows from the origin, plus a unit circle (`theta = np.linspace(0, 2*np.pi, 100)`, `plt.plot(np.cos(theta), np.sin(theta))`). Visually confirm the normalized arrow's tip lands exactly on the circle.

**Why this matters:** real embedding models (e.g., OpenAI/Cohere/sentence-transformer embeddings) are often normalized to unit length before being stored in a vector database, specifically so that cosine similarity search reduces to a simple dot product. Normalizing embeddings is a real, common preprocessing step in production RAG systems — not just a math exercise.

---

## Section D — Norms & Visualization

### Q6. L1 vs. L2 Norm — and Their "Shape"
Given a toy embedding `v = np.array([3, -4, 12])`:

1. Compute the **L2 norm** two ways: `np.linalg.norm(v)` and manually via `np.sqrt(np.sum(v**2))`. Confirm they match. (This L2 norm is the exact "embedding magnitude" you'd check before deciding whether to normalize an embedding for RAG.)
2. Compute the **L1 norm** two ways: `np.linalg.norm(v, ord=1)` and manually via `np.sum(np.abs(v))`.
3. Now, for **visualization**, work in 2D. Generate ~2000 random 2D points spread across `[-2, 2] x [-2, 2]` (`np.random.uniform`), compute the L1 norm and L2 norm of every point (`axis=1`), and use `plt.scatter` with `c=` set to each norm to produce **two side-by-side plots** (`plt.subplot(1, 2, 1)` / `(1, 2, 2)`) colored by norm value. You should visually see circular contours for L2 and diamond-shaped contours for L1.

**Why this matters:** those circle vs. diamond contours are *exactly* why L2 regularization (Ridge) shrinks weights smoothly while L1 regularization (Lasso) tends to zero some weights out — the same regularization techniques used when fine-tuning GenAI models to prevent overfitting.

---

## Section E — Matrices & Visualization (a.k.a. transformer building blocks)

### Q7. Creating & Inspecting an Embedding Table
1. Create a 3×3 matrix `A` containing the numbers 1–9 (in order) using `np.arange` and `.reshape` — pretend this is a tiny embedding table for 3 tokens, each with a 3-dimensional embedding.
2. Print its `.shape`, `.ndim`, and `.T` (transpose).
3. Create a 3×3 identity matrix using `np.eye(3)` (this is what an "unchanged" transformation looks like — you'll meet this again if you ever study residual/skip connections), and a 3×3 matrix of random integers 1–10 using `np.random.randint`.
4. Extract: token 0's full embedding (first row), the last "feature column" across all tokens, and the single value at row 1, column 2.
5. **Visualize `A`** with `plt.imshow(A, cmap='viridis')` plus `plt.colorbar()`, and annotate each cell with its numeric value using `plt.text`. This "matrix as an image" view is exactly how you'll eventually inspect real embedding tables and attention weight matrices.

---

### Q8. Matrix Operations — Query · Key Attention, at Matrix Scale
Given two tiny "embedding" matrices (2 tokens, each with a 2-dim embedding):
```python
Q = np.array([[1, 2],
              [3, 4]])   # "query" vectors for 2 tokens
K = np.array([[5, 6],
              [7, 8]])   # "key" vectors for 2 tokens
```
Compute each of the following and, for each, state in one line whether the result is elementwise or a "true" matrix operation:
1. `Q + K`
2. `Q * K` (elementwise product — **not** the same as matrix multiplication!)
3. `Q @ K.T` (true matrix multiplication — **this produces a full attention score matrix**, i.e. every token's query dotted with every token's key, all at once). Confirm it matches `np.matmul(Q, K.T)`.
4. The determinant of `Q` via `np.linalg.det`.
5. The inverse of `Q` via `np.linalg.inv`, confirming `Q @ np.linalg.inv(Q)` ≈ identity.

**Common bug alert:** mixing up `*` and `@` is one of the most frequent silent bugs in ML/GenAI code — `*` runs without error but gives you the *wrong math*. In a real transformer, using `*` instead of `@` here would silently break attention entirely. Always double-check which one you mean.

---

### Q9. Visualizing a Matrix as a Transformation (a.k.a. what a projection layer does)
A matrix isn't just a grid of numbers — it's a function that transforms vectors. In a transformer, the **Query, Key, and Value projection matrices** each take an input embedding and transform it into a new space. Given:
```python
W_projection = np.array([[2, 0],
                          [0, 1]])          # a toy "projection matrix", stretches x, leaves y alone
```
1. Create a set of points forming a unit square: `square = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])` (think of these 4 corner points as 4 tiny 2D "embeddings").
2. Apply the transformation: `transformed = square @ W_projection.T`.
3. **Plot both the original square and the transformed square** on the same axes (`plt.plot`, equal aspect ratio) in different colors, so you can see exactly how `W_projection` reshaped the space.
4. Repeat with a rotation matrix instead:
$$R = \begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix}, \quad \theta = 45°$$
and plot the rotated square.

**Why this matters:** every Q/K/V projection, every feed-forward layer, and every attention head in a transformer is fundamentally a matrix reshaping embedding space like this — just in hundreds of dimensions instead of 2. This exercise makes that abstract idea visible and concrete.

---

### Q10. Putting It Together — A Mini Transformer Feed-Forward Layer
This simulates a **single feed-forward layer inside a transformer block** — exactly what sits after the attention mechanism in every GPT-style model.

Given:
- A batch of 4 tokens, each with a 3-dimensional embedding after attention: `X` of shape `(4, 3)` (random values).
- A weight matrix `W` of shape `(3, 2)` (random values) — projecting each 3-dim token embedding down to 2 dimensions.
- A bias vector `b` of shape `(2,)` (random values).

1. Compute the layer's output: `Z = X @ W + b`.
2. Print the shape of `Z` and explain *why* it has that shape (in terms of the shapes of `X`, `W`, `b`, and broadcasting).
3. Compute the L2 norm of each of the 4 output rows in `Z` **without a for-loop** (hint: the `axis` parameter of `np.linalg.norm`) — one "activation strength" score per token.
4. **Plot a bar chart** (`plt.bar`) of the 4 row-norms, one bar per token, labeled "Token 1"–"Token 4".
5. **Bonus — a taste of RAG:** treat each row of `Z` as if it were 4 candidate document embeddings, and treat `b` (reshaped/extended, or just pick one row of `Z` as a stand-in "query") as a query embedding. Using the `normalize` function from Q5 and the dot-product idea from Q4, compute the cosine similarity between the query and each of the 4 rows, and print which "document" is the most relevant match.

**This is not a toy exercise** — `Z = X @ W + b` is the literal formula for a dense/feed-forward layer in every transformer implementation (PyTorch, TensorFlow, Hugging Face). If you understand this line — and the retrieval step in part 5 — deeply, you understand the two mathematical cores of modern GenAI: **transformers and RAG.**

---

## Self-Check Summary

| # | Topic | GenAI connection | Key function(s) |
|---|-------|-------------------|------------------|
| 1 | Scalar vs vector | A token embedding IS a vector | `np.array`, `.shape`, `.ndim` |
| 2 | Vector construction | Building/initializing an embedding table | `np.arange`, `np.linspace`, `np.random.randn` |
| 3 | Elementwise ops | Positional encoding = embedding + position vector | `+ - * / **`, broadcasting |
| 4 | Dot product + angle | Core of self-attention & cosine similarity | `np.dot`, `@`, `plt.quiver`, `np.arccos` |
| 5 | Unit vectors | Normalizing embeddings before vector search | vector / its norm, `plt.plot` unit circle |
| 6 | L1 / L2 norms | Regularization when fine-tuning models | `np.linalg.norm(v, ord=...)`, `plt.scatter` |
| 7 | Matrix basics | Embedding table as a matrix | `.reshape`, `np.eye`, indexing, `plt.imshow` |
| 8 | Matrix ops | Full attention score matrix `Q @ K.T` | `*` vs `@`, `np.linalg.det`, `np.linalg.inv` |
| 9 | Matrix as transformation | Q/K/V projection layers | `.T`, rotation matrix, `plt.plot` before/after |
| 10 | Feed-forward layer + RAG | Transformer FFN + document retrieval | `X @ W + b`, cosine similarity, `plt.bar` |

---

<details>
<summary><strong>💡 Click to reveal hints & solution sketches (try the questions first!)</strong></summary>

```python
import numpy as np
import matplotlib.pyplot as plt

# Q1
temperature = 0.7
t_arr = np.array(0.7)
king_embedding = np.array([0.21, -0.05, 0.88, 0.14])
print(t_arr.shape, t_arr.ndim)          # () 0  -> a true scalar has NO axes at all
print(king_embedding.shape, king_embedding.ndim)   # (4,) 1

# Q2
token_ids = np.arange(10)
spaced = np.linspace(0, 1, 5)
pad_zeros = np.zeros(6); pad_ones = np.ones(6)
embedding_table = np.random.randn(5, 4)   # 5 tokens, 4-dim embeddings
print(embedding_table.shape)              # (5, 4)

# Q3
a = np.array([1, 2, 3, 4]); b = np.array([5, 6, 7, 8])
a + b, a - b, a * b, a / b, a**2, (a - b)**2

# Q4
query = np.array([3, 4]); key = np.array([4, 3])
total = sum(x*y for x, y in zip(query, key))
assert total == query @ key == np.dot(query, key)

fig, ax = plt.subplots()
ax.quiver(0, 0, *query, angles='xy', scale_units='xy', scale=1, color='b', label='query')
ax.quiver(0, 0, *key, angles='xy', scale_units='xy', scale=1, color='r', label='key')
ax.set_xlim(-1, 6); ax.set_ylim(-1, 6); ax.set_aspect('equal'); ax.legend()
cos_theta = (query @ key) / (np.linalg.norm(query) * np.linalg.norm(key))
angle_deg = np.degrees(np.arccos(cos_theta))
ax.text(0.5, 5, f"angle = {angle_deg:.1f} deg")
plt.show()

# Q5
def normalize(vec):
    return vec / np.linalg.norm(vec)

v = np.array([3, 4]); v_hat = normalize(v)
theta = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots()
ax.plot(np.cos(theta), np.sin(theta), 'g--', label='unit circle')
ax.quiver(0, 0, *v, angles='xy', scale_units='xy', scale=1, color='b', label='v')
ax.quiver(0, 0, *v_hat, angles='xy', scale_units='xy', scale=1, color='r', label='v_hat')
ax.set_xlim(-5, 5); ax.set_ylim(-5, 5); ax.set_aspect('equal'); ax.legend()
plt.show()

# Q6
v = np.array([3, -4, 12])
l2 = np.linalg.norm(v)
l1 = np.linalg.norm(v, ord=1)

pts = np.random.uniform(-2, 2, size=(2000, 2))
l1_norms = np.linalg.norm(pts, ord=1, axis=1)
l2_norms = np.linalg.norm(pts, ord=2, axis=1)
plt.subplot(1, 2, 1); plt.scatter(pts[:,0], pts[:,1], c=l1_norms, s=5); plt.title("L1 norm"); plt.gca().set_aspect('equal')
plt.subplot(1, 2, 2); plt.scatter(pts[:,0], pts[:,1], c=l2_norms, s=5); plt.title("L2 norm"); plt.gca().set_aspect('equal')
plt.show()

# Q7
A = np.arange(1, 10).reshape(3, 3)
plt.imshow(A, cmap='viridis'); plt.colorbar()
for i in range(3):
    for j in range(3):
        plt.text(j, i, A[i, j], ha='center', va='center', color='white')
plt.show()

# Q8
Q = np.array([[1, 2], [3, 4]]); K = np.array([[5, 6], [7, 8]])
Q + K          # elementwise
Q * K          # elementwise (Hadamard)
attention_scores = Q @ K.T    # true matrix multiplication -> full attention score matrix
np.array_equal(attention_scores, np.matmul(Q, K.T))
np.linalg.det(Q)
np.linalg.inv(Q) @ Q   # approx identity

# Q9
W_projection = np.array([[2, 0], [0, 1]])
square = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
transformed = square @ W_projection.T
plt.plot(square[:,0], square[:,1], 'b-o', label='original')
plt.plot(transformed[:,0], transformed[:,1], 'r-o', label='transformed')
plt.gca().set_aspect('equal'); plt.legend(); plt.show()

theta = np.radians(45)
R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
rotated = square @ R.T
plt.plot(square[:,0], square[:,1], 'b-o', label='original')
plt.plot(rotated[:,0], rotated[:,1], 'g-o', label='rotated 45deg')
plt.gca().set_aspect('equal'); plt.legend(); plt.show()

# Q10
X = np.random.randn(4, 3)     # 4 tokens, 3-dim embeddings
W = np.random.randn(3, 2)
b = np.random.randn(2)
Z = X @ W + b                 # (4,3)@(3,2) -> (4,2), then b (2,) broadcasts across rows
row_norms = np.linalg.norm(Z, axis=1)
plt.bar([f"Token {i+1}" for i in range(4)], row_norms)
plt.ylabel("L2 norm of output row"); plt.show()

# Bonus: cosine-similarity "retrieval" over the 4 rows of Z
query_vec = Z[0]                       # pretend row 0 is our "query"
candidates = Z[1:]                     # pretend rows 1-3 are "documents"
sims = [normalize(query_vec) @ normalize(doc) for doc in candidates]
best_match = np.argmax(sims)
print("similarities:", sims)
print(f"Most relevant document: Token {best_match + 2}")   # +2 because we sliced off row 0 and index from 0
```
</details>

---

*Next up once you're comfortable with this sheet: broadcasting rules in depth, `np.sum`/`np.mean` with `axis`, softmax over attention scores, and gradient computations — the last building blocks before your first transformer.*

*Companion files: `statistics_for_ml_dl_genai_guide.md`, `statistics_teaching_guide_with_code.md`, and `numpy_vectors_matrices_SOLUTIONS_teacher.md` (answer key for the original version of this sheet — ask if you'd like an updated GenAI-flavored teacher's key too).*

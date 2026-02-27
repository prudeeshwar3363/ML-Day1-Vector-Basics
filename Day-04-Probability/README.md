# 📘 Day 04 – Probability & Bayes Theorem

## 📅 Date
27-02-2025

---

## 🎯 Objective

To understand:

- Basic Probability
- Conditional Probability
- Bayes Theorem
- How probability connects to Machine Learning

---

# 📚 Theory Summary

## 🔹 Probability

Probability measures how likely an event is to occur.

\[
P(A) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}}
\]

Range:  
0 → Impossible  
1 → Certain  

---

## 🔹 Conditional Probability

Probability of A occurring given B has already occurred.

\[
P(A|B) = \frac{P(A \cap B)}{P(B)}
\]

This helps us update probability based on new information.

---

## 🔹 Bayes Theorem

\[
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
\]

Used to reverse conditional probabilities.

---

## 🔹 ML Connection

Machine Learning classifiers estimate:

\[
P(Class | Features)
\]

Naive Bayes classifier uses Bayes Theorem to compute:

Probability that an email is spam given words in the email.

---

# 💻 Task Implementations

---

## 🔹 Task 1 – Basic Probability

```python
def probability(favorable, total):
    return favorable / total

print("Coin Toss Probability (Heads):", probability(1, 2))
print("Dice Probability (Rolling 3):", probability(1, 6))
```

## ✅ Output

```python
Coin Toss Probability (Heads): 0.5
Dice Probability (Rolling 3): 0.16666666666666666
```

## 🔹 Task 2 – Conditional Probability

Scenario:
- Total Students = 100
- Engineers = 60
- Engineers who know Python = 30

\[
P(Python|Engineer) = 30/60
\]

```python
def conditional_probability(intersection, given):
    return intersection / given

print("P(Python | Engineer):", conditional_probability(30, 60))
```

## ✅ Output

```python
P(Python | Engineer): 0.5
```
Meaning: 50% of engineers know Python.

## 🔹 Task 3 – Bayes Theorem

Medical Example:
- P(Disease) = 0.01
- P(Positive | Disease) = 0.99
- Assume P(Positive) ≈ 0.02

```python
def bayes(p_b_given_a, p_a, p_b):
    return (p_b_given_a * p_a) / p_b

p_disease = 0.01
p_positive_given_disease = 0.99
p_positive = 0.02

result = bayes(p_positive_given_disease, p_disease, p_positive)

print("P(Disease | Positive Test):", round(result, 4))
```

## ✅ Output

```python
P(Disease | Positive Test): 0.495
```
Even with 99% accurate test, probability is ~49.5%.
This shows how rare events affect predictions.

## 🔹 Task 4 – Key Questions Answered

### Why can rare events mislead predictions?
If an event is very rare, even small false positives can drastically change final probability.

### Why is P(A|B) different from P(B|A)?
Because the condition changes the denominator.
Probability direction matters.

### How is Bayes used in spam classification?
It calculates probability of spam given words in email using prior probabilities and likelihood.

## 📊 Observations

- Probability direction matters.
- Rare events significantly affect predictions.
- Bayes Theorem explains many classification models.
- ML models are essentially probability estimators.

## 🧠 Key Takeaways

- Probability is foundation of classification.
- Conditional probability updates beliefs.
- Bayes Theorem helps reverse probabilities.
- Understanding this improves ML intuition.

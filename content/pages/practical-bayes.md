title: Practical Bayes

The Practical Bayes course was first held at [Moscow State University, Autumn 2022](https://www.econ.msu.ru/students/mag/curricula/eco/andan/news/News.20220802192752_5070/)

This course is aimed at mastering Bayesian methods in practice. 
Advanced modeling is not about conjugate distributions (although they are sometimes useful), but mostly about projecting knowledge about the problem into code. 
Successful research will also require skills in solving problems of convergence, parameterization, selection from several models. A course with a focus on programming in Python / PyMC.

## Lecture 1
Introducing Bayesian thinking and practical definitions of the famous Bayes formula

$$
p(\theta|\;\mathcal{D}) = \frac{p(\mathcal{D}|\;\theta)p(\theta)}{p(\mathcal{D})}
$$

### Priors
Everything starts with good priors $p(\theta)$ where you put your business knowledge into the model.
Priors often mean that you think of the model, the parameters meaning, causal graph.
Often claimed subjective nature of the priors usually improves the overall quality of the analysis. 
Good priors usually mean they can be explained in words to non math audience.

#### Example 1
You are a researcher conducting an AB test. 
You test your new approach and expect an improvement. Compare these model priors:

1. A non subjective prior where the the improvement may vary from $-100\%$ to $+\infty\%$, may be any.
2. An informed prior where the improvement is within $-5\%$ and $+5\%$.

A more informed prior is subjective, based on past experience but makes more sense compared to a non informed prior.

#### Example 2
You are an economist estimating elasticity. Compare these two priors:

1. Elasticity may be any positive number, from $0$ to $+\infty\%$.
2. Elasticity is positive and is for sure no more than 3.

A more informed prior is subjective, depends on a product, optimism, historical data and conforms with past research 

### Likelihood and model structure
<image src="/images/bias-variance.png" style="width: 100%">
A likelihood can be treated informally as nuances of observational model you take in account.
A likelihood may be simplifying or complex, of overly-complicated.
These nuances are outliers, time dependencies, correlations in observations and so on.
The more complicated is likelihood and model structure, the less strict assumptions are present in the model.
Every next block there is a relaxed assumption which, in turn, needs a new prior to constrain variation of the model.

#### Example 1
You observational model may contain zeros, e.g. you sell many products and study history of a single one.

<div class="image-comment">
<style>
@media (min-width: 540px) {
    .image-comment .image {
        max-width: 10%; 
        min-width: 100px;
    }
}
</style>
<div class="image">
<image src="/images/shop.png">
</div>
<div class="comment">
\begin{align*}
        \text{make an order} &\sim \operatorname{Bernoulli}(p) \\
        \text{order amount} &\sim \begin{cases}
        \operatorname{Gamma}(\alpha, \beta)&, \text{make an order} = 1\\
        0&, \text{make an order} =0
        \end{cases}
\end{align*}
</div>
</div>
#### Example 2
In most cases it is satisfactory to start simple and relax assumptions.

1. Assume your time series model does not have seasonality and outliers, estimate it.
2. At this point you have a better understanding of the limitations you had at the previous step, introduce seasonality, reuse as much as possible.

![airlines](/images/airline_passengers.png)


> More at the [Presentation](/latex/beamer/practical-bayes/lecture-1/lecture-1.pdf)


## Lecture 2
More at the [Presentation](/latex/beamer/practical-bayes/lecture-2/lecture-2.pdf)

## Lecture 3
More at the [Presentation](/latex/beamer/practical-bayes/lecture-3/lecture-3.pdf)

## Lecture 4
More at the [Presentation](/latex/beamer/practical-bayes/lecture-4/lecture-4.pdf)

## Lecture 5
More at the [Presentation](/latex/beamer/practical-bayes/lecture-5/lecture-5.pdf)

## Lecture 6
More at the [Presentation](/latex/beamer/practical-bayes/lecture-6/lecture-6.pdf)

title: Practical Bayes

The Practical Bayes course was first held at [Moscow State University, Autumn 2022](https://www.econ.msu.ru/students/mag/curricula/eco/andan/news/News.20220802192752_5070/)

This course is aimed at mastering Bayesian methods in practice. 
Advanced modeling is not about conjugate distributions (although they are sometimes useful), but mostly about projecting knowledge about the problem into code. 
Successful research will also require skills in solving problems of convergence, parameterization, selection from several models. A course with a focus on programming in Python / PyMC.

## Lecture 1
Introducing Bayesian thinking and practical definitions of the famous Bayes formula.

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
<!-- <style>
@media (min-width: 540px) {
    .image-comment .image {
        max-width: 10%; 
        min-width: 100px;
    }
}
</style> -->
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

<image src="/images/airline_passengers.png" style="width: 100%">


<b>More in the [Presentation](/latex/beamer/practical-bayes/lecture-1/lecture-1.pdf)</b>


## Lecture 2

Hierarchical modelling.

### Classical Econometrics view:

* All the groups are independent and treated similarly. **Pooled Model**

$$
    y_{k,i} = \alpha + \beta x_{k,i} + \varepsilon_{i,k}
$$

* Groups have non significant, random differences. **Random Effects Model**

$$
    y_{k,i} = \alpha + \beta x_{k,i} + u_{k} + \varepsilon_{i,k}
$$


* Groups have significant differences. **Fixed Effect Model**

$$
    y_{k,i} = \alpha_{k} + \beta x_{k,i} + \varepsilon_{i,k}
$$

### Bayesian Hierarchy

Bayesian modelling allows to interpolate between pooled, fixed and random effect models.
What you do as a modeller, you set a prior that tells the model which interaction strength you assume.

#### Example

* You model a country macroeconomic or marketing model, you might assume that countries have similar behavior, yet different.
* You model region level marketing model, compared to the previous example differences between regions are considered smaller, yet outliers may appear.

These two cases differ by the perceived strength of similarity.
In the traditional econometrics you only have a hard switch between model types.
Bayesian modelling provides you with the one model it is called Hierarchical.
It provides you with a "slider" to interpolate between *Pooled Model* and *Fixed Effects Model* extreme cases.
Whenever you see "Hierarchical Bayesian model", think of a classical econometrics and multiple subjects.
Prior specification will allow you to choose the right spot.

<b>More in the [Presentation](/latex/beamer/practical-bayes/lecture-2/lecture-2.pdf)</b>

## Lecture 3
AB testing.

The world of AB testing is huge and I don't attempt (yet) to cover all the possible scenarios.
What I do is translate the classical AB testing workflow into Bayesian framework.
The big picture is you

1. Prepare the experiment and the baseline.
2. Plan the experiment, its duration and the success criteria.
3. Collect the results on completion, interpret.

All the 3 steps are extremely well studied and applied in every mature company.
However, there are inconsistencies as well as missed opportunities in planning and interpretation.

### Preparation
While experiment preparation a Bayesian modeller should ask questions to set priors.
These questions are related to the experiment outcomes and are highly business oriented.
While two distant parties interact, Business and Analytics, they have common touch points, the priors.

* Do you expect after changes in B you have a 100% increase? Very sure No
* Do you expect after changes in B you have a 1000% increase? Very sure No
* Do you expect after changes in B you have a 10% increase? Unlikely
* Do you expect after changes in B you have a 3% increase? Maybe
* Do you expect after changes in B you have a 3% decrease? Maybe
* Do you expect after changes in B you have an X% decrease? Your answer

Questions are easy to ask and they very are much related to the core model.
Bayesian approach allows to link Business people to the Math people.
Right questions matter.

### Planning

<div class="image-comment">
<div class="image">
<image src="/images/fast_accurate.png">
</div>
<div class="comment">

Planning is little different from the <a href="https://en.wikipedia.org/wiki/Power_of_a_test">power analysis</a> from a classical approach.
Both alternatives solve the same problem

</div>
</div>

* What is the required number of observations to make a conclusion?
* What is the quality of the conclusion if I make a decision after seeing N observations?

> The impossibility principle. You can't be fast in data collection and accurate at the same time.


### Interpretation
<image src="/images/confidence-intervals.png" style="width: 100%">

The confidence interval is overused and overly-simplified in my opinion.
Thus, it is often interpreted incorrectly.
The correct but not very intuitive interpretation can be found in an [explanation by Joe Felsenstein](https://evolution.gs.washington.edu/gs560/2011/lecture3.pdf)

> You could say that if you do this throughout your career, 95% of these intervals will contain the true value.

The Bayesian posterior allows for a targeted questioning.
You can directly "ask" the model simple questions like:

* What is the probability experiment uplift is greater than zero?
* What is the probability experiment uplift is greater than 3%?
* What is the 5% [value at risk](https://en.wikipedia.org/wiki/Value_at_risk) of the experiment uplift?

More complex multi-experiment questions:

* What is the probability experiment A is better than B?
* What is the probability experiment A is the best among A, B, C and D?

Advanced questions are not complicated are few lines of code as well (given you know how to translate uplift to profit amounts):

* What is the expected profit from implementing A? Or B?
* What is the 5% value at risk profit implementing A?
* What is the 95% interval of most probable profit implementing A?

<b>More in the [Presentation](/latex/beamer/practical-bayes/lecture-3/lecture-3.pdf)</b>

## Lecture 4
<b>More in the [Presentation](/latex/beamer/practical-bayes/lecture-4/lecture-4.pdf)</b>

## Lecture 5
<b>More in the [Presentation](/latex/beamer/practical-bayes/lecture-5/lecture-5.pdf)</b>

## Lecture 6
<b>More in the [Presentation](/latex/beamer/practical-bayes/lecture-6/lecture-6.pdf)</b>

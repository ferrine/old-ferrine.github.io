Title: Distributions

This is an inspirationally WIP page

..graphviz dot
digraph G {
    node [shape=box];
    start [label="Likelihood or Prior?"];
    likelihood [label="Is your data Discrete or Continuous?"];
    prior [label="Is your parameter Discrete or Continuous?"];
    discrete_likelihood [label="Type of data"];
    dimensions [label="Scalar data?"];
    choice [label="Choice data", shape=ellipse];
    count [label="Count data", shape=ellipse];
    geometric [label="Geometric", shape=ellipse];
    bernoully [label="Bernoully", shape=ellipse];
    multiple_choice [label="Categorical", shape=ellipse];
    zero_inflated_count [label="Zero inflation?"];
    poisson [label="Poisson", shape=ellipse];
    zero_inflated_poisson [label="ZeroInflatedPoisson", shape=ellipse];
    start -> likelihood [label="Likelihood"];
    start -> prior [label="Prior"];
    likelihood -> dimensions [label="Continuous"];
    likelihood -> discrete_likelihood [label="Discrete"];
    discrete_likelihood -> choice;
    discrete_likelihood -> count;
    choice -> bernoully [label="Binary"]
    choice -> multiple_choice [label="Multiple Choice"];
    count -> zero_inflated_count [label="Number of Events"];
    zero_inflated_count -> poisson [label="No"];
    zero_inflated_count -> zero_inflated_poisson [label="Yes"];
    count -> geometric [label="Repeated Success"];
}

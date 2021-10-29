Title: Distributions


..graphviz dot
digraph G {
    node [shape=box];
    start [label="Likelihood or Prior?"];
    likelihood [label="Is your data Discrete or Continuous?"];
    prior [label="Is your parameter Discrete or Continuous?"];
    discrete_likelihood [label="Type of data"];
    tails [label="Does your data have outliers?"];
    choice [label="Choice data", shape=ellipse];
    bernoully [label="Bernoully", shape=ellipse, URL="https://google.com"];
    start -> likelihood [label="Likelihood"];
    start -> prior [label="Prior"];
    likelihood -> tails [label="Continuous"];
    likelihood -> discrete_likelihood [label="Discrete"];
    discrete_likelihood -> choice;
    choice -> bernoully [label="Binary"]
}

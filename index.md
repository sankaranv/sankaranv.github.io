---
layout: index
title: Main Page
sidebar_link: false
---

<style>

table {
  margin-bottom: 1rem;
  width: 100%;
  font-size: 80%;
  border: 0px solid rgba(0, 0, 0, 0);
  border-collapse: collapse;
}

td,
th {
  padding: 1rem .25rem;
  border: 0px solid $border-color;
}

th {
  text-align: left;
}

tbody tr:nth-child(odd) td,
tbody tr:nth-child(odd) th {
  background-color: transparent;
}

paper {
 color: #; 
 font-weight:bold;
}

</style>

I am a PhD student at the [College of Information and Computer Sciences, UMass Amherst](https://www.cics.umass.edu/), where I am advised by [David Jensen](https://people.cs.umass.edu/~jensen/). My research aims to create tools for analyzing the behaviour of complex AI systems, with a focus on problems in explanation, blame attribution, and safety evaluation. To this end, my research interests span the areas of causal inference, reinforcement learning and probabilistic machine learning.

Before coming to UMass, I worked on clustering algorithms for large hypergraphs at the [Indian Institute of Technology Madras](https://www.iitm.ac.in/), where I was advised by [Prof. Balaraman Ravindran](https://www.cse.iitm.ac.in/~ravi/). I graduated with a B.E in Electrical and Electronics Engineering from [SSN College of Engineering](http://www.ssn.edu.in/), affliated to [Anna University](https://www.annauniv.edu/).

My publications can be found on [Google Scholar](https://scholar.google.com/citations?user=DbeHYRcAAAAJ&hl=en&oi=sra).
## Research

<table width="100%" align="center" border="0" cellspacing="0" cellpadding="20">


<tr>
       <td width="16%"  valign="top">
            <img src="/images/projects/IVP.png" alt="lean" style="vertical-align:center; horiz-align:left; width: 100%; margin:0px 0px; border-radius:0%"/> 
     </td>
     <td valign="top" width="65%">
          <p>
              <paper>Automated Discovery of Functional Actual Causes in Complex Environments</paper>
                <br>
                <a href='http://calcharles.github.io/'>Caleb Chuck<sup>*</sup></a>,
                <b>Sankaran Vaidyanathan<sup>*</sup></b>,    
                <a href='https://sgiguerecs.com/'>Stephen Giguere</a>,
                <a href='https://amyzhang.github.io/'>Amy Zhang</a>,
                <a href='https://people.cs.umass.edu/~jensen/'>David Jensen</a>,
                <a href='https://people.cs.umass.edu/~sniekum/'>Scott Niekum</a>
                <br>
       <i>In preparation</i> | <a href='https://arxiv.org/pdf/2404.10883.pdf'>arXiv</a>
       <br><br>
       Classical definitions of actual causation often declare a large number of events and entities in an environment to be causes, even when many of them rarely influence the outcome. This is an issue of <i>normality</i>, or the distinction between normal and rare events as potential causes. By exploiting <i>context-specific independencies</i> in the environment, we can prune out events that do not affect the outcome in the observed context and identify a restricted and focused set of actual causes. We accordingly extend the formal definition of actual causation and show how to automatically infer actual causes under this definition.
          </p>  
     </td>
   </tr>

</table>

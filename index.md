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

I am a PhD student at the [College of Information and Computer Sciences, UMass Amherst](https://www.cics.umass.edu/), where I am advised by [David Jensen](https://people.cs.umass.edu/~jensen/). My research spans the areas of causal inference, probabilistic machine learning, and reinforcement learning. I aim to create tools for analyzing and evaluating the behavior of complex AI systems, with a focus on problems in blame and responsibility attribution, explainability, and alignment with human norms. I am also interested in causal inference methods for evaluation and mechanistic interpretability in large language models. 

Unlike most applications of causal inference that involve objective experimentation and interaction with the external world, these issues are traditionally grounded in subjective human judgments. These involve <b>norms</b> that can be very counterintuitive and pose a significant challenge to purely statistical approaches in causal inference. By developing formal approaches for modeling norms and inference algorithms that align with norms, I hope to support open and scientific evaluation and auditing of AI systems, and the growth of AI systems that better align with norms. 

For a complete list of my publications, see my [Google Scholar](https://scholar.google.com/citations?user=DbeHYRcAAAAJ&hl=en&oi=sra).

## Research

<table width="100%" align="center" border="0" cellspacing="0" cellpadding="20">


<tr>
       <td width="20%"  valign="top">
            <img src="/images/projects/IVP.png" alt="lean" style="vertical-align:center; horiz-align:left; width: 100%; margin:0px 0px; border-radius:0%"/> 
     </td>
     <td valign="top" width="65%">
          <p>
              <paper>Automated Discovery of Functional Actual Causes in Complex Environments</paper>
                <br>
                <a href='http://calcharles.github.io/'>Caleb Chuck*</a>,
                <b>Sankaran Vaidyanathan*</b>,    
                <a href='https://sgiguerecs.com/'>Stephen Giguere</a>,
                <a href='https://amyzhang.github.io/'>Amy Zhang</a>,
                <a href='https://people.cs.umass.edu/~jensen/'>David Jensen</a>,
                <a href='https://people.cs.umass.edu/~sniekum/'>Scott Niekum</a>
                <br>
       <i>In preparation</i> | <a href='https://arxiv.org/pdf/2404.10883.pdf'>arXiv</a>
       <br><br>
       Classical definitions of actual causation often declare a large number of events and entities in an environment to be causes, even when many of them rarely influence the outcome. This is an issue of <i>normality</i>, or the distinction between normal and rare events as potential causes. By exploiting <i>context-specific independencies</i> in the environment, we can prune out events that do not affect the outcome in the observed context and identify a restricted and focused set of actual causes. We extend the formal definition of actual causation to account for these independencies and show how to automatically infer actual causes under this definition.
          </p>  
     </td>
   </tr>

<tr>
       <td width="20%"  valign="top">
            <img src="/images/projects/judge.png" alt="lean" style="vertical-align:center; horiz-align:left; width: 100%; margin:0px 0px; border-radius:0%"/> 
     </td>
     <td valign="top" width="65%">
          <p>
              <paper>Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges</paper>
                <br>
                <a href='https://www.linkedin.com/in/singh96aman/'>Aman Singh Thakur*</a>,
                <a href='https://www.mlbykartik.com/'>Kartik Choudhary*</a>,
                <a href='https://www.linkedin.com/in/venkat-srinik-ramayapally-18565a170/'>Venkat Srinik Ramayapally*</a>,
                <b>Sankaran Vaidyanathan</b>,    
                <a href='https://dieuwkehupkes.nl/'>Dieuwke Hupkes</a>,
                <br>
       <i>In preparation</i> | <a href='https://arxiv.org/abs/2406.12624'>arXiv</a>
       <br><br>
       Large language models are often evaluated using the <i>LLM-as-a-judge paradigm</i>, but there are still many open questions about the evaluation paradigm itself. We evaluate various LLMs acting as judges using human annotations on a controlled setup using the TriviaQA benchmark. <b>(1)</b> Only GPT-4 Turbo and Llama3-70B shine among all the judge models we evaluate, but their alignment with human annotations still falls short of inter-human annotator agreement. <b>(2)</b> Scores assigned by judges with >80% percent human alignment can be ~20 points apart, and Cohen's kappa is a superior metric. <b>(3)</b> Most aligned in scores != most discriminative, sometimes judge models with low human alignment such as JudgeLM-7B and Contains (lexical match) outperform larger and more aligned models in terms of <i>ranking</i> models, since their biases are more systematic. <b>(4)</b> Judge LLMs are often lenient and can be easily tricked by controlled responses like "Yes," "Sure," and "I don't know". <b>(5)</b> It is not easy to steer large models, but smaller models get confused by adding too much detail. Overall, we urge caution in trusting LLMs as judges without including an evaluation of the judges themselves: 
      </p>
     </td>
   </tr>

</table>

---
layout: index
sidebar_link: false
---

I work at the [Indian Institute of Technology Madras](https://www.iitm.ac.in/) as a Project Associate, and am fortunate to be advised by [Prof. Balaraman Ravindran](https://www.cse.iitm.ac.in/~ravi/). I am associated with the [Robert Bosch Centre for Data Science and Artificial Intelligence](https://rbc-dsai.iitm.ac.in/) and the [RISE-IIL Lab](https://rise-iil.github.io). 

My research lies in the area of machine learning on graphs; my primary work is on hypergraph clustering with modularity and spectral methods. In the process, I was also fortunate to work in collaboration with [Prof. Srinivasan Parthasarathy](http://web.cse.ohio-state.edu/~parthasarathy.2/), The Ohio State University. I previously worked on end-to-end clustering with deep neural networks, and a little bit of reinforcement learning. I enjoy looking for inspiration from psychology, philosophy and the arts as well. 

Prior to this, I graduated with a B.E in Electrical and Electronics Engineering from [SSN College of Engineering](http://www.ssn.edu.in/), affliated to [Anna University](https://www.annauniv.edu/). Before that, I spent time writing theatrical plays and thinking about how to connect disparate elements with stories.

## Projects

<table width="100%" align="center" border="0" cellspacing="0" cellpadding="20">
   <tr>
     <td valign="top" width="85%">
          <p>
              <paper><b>A New Measure of Modularity on Hypergraphs: Theoretical Insights and Implications for Effective Clustering</b></paper>
              <br>
              Tarun Kumar*, 
              <b>Sankaran Vaidyanathan*</b>, 
              <a href='https://www.linkedin.com/in/harinianantha/'>Harini Ananthapadmanabhan</a>,  
              <a href='http://web.cse.ohio-state.edu/~parthasarathy.2/'>Srinivasan Parthasarathy</a>, 
              <a href='https://www.cse.iitm.ac.in/~ravi/'>Balaraman Ravindran</a>
              <br>
              <i>(under review, preprint coming soon!)</i>
              <!-- [<a href="">Arxiv</a>, <a href="">Code</a>] -->
              <details>
                <summary>Abstract</summary>            
                  <p class="message">
                    Learning on graphs is a field of great interest due to the abundance of relational data from real-world systems. However, many such systems consist of entities that exhibit more complex group interactions rather than simple pairwise relationships; examples of these are co-authorship, co-citation and protein complex networks. Such super-dyadic relations are more suitably modeled using hypergraphs. Learning on hypergraphs has thus been garnering increased attention with potential applications in network analysis, VLSI design and computer vision, among others. Our primary contribution in this work is to generalize the framework of modularity maximization for clustering on hypergraphs. In doing this, we introduce a hypergraph null model that can be shown to correspond exactly to the configuration model for undirected graphs. We derive an adjacency matrix reduction that preserves the hypergraph node degree sequence, for use with this null model. The resultant modularity function may be maximized using the Louvain method, which is a popular fast algorithm known to work well in practice for graphs. We additionally propose a refinement over this clustering that exploits higher-order information within the hypergraph. This works by iteratively reweighting cut hyperedges, based on the proportion of their nodes in different communities. We demonstrate both the efficacy and efficiency of our methods on several real-world datasets.
                  </p>
              </details>
          </p>  
     </td>
   </tr>
</table>

## Courses

- [CS 7015: Deep Learning](https://www.cse.iitm.ac.in/~miteshk/CS7015.html)
- [CS 6730: Probabilistic Graphical Models](https://sites.google.com/site/harishguruprasad/teaching/cs6730pgm)

## Lab talks

- **A Tour of Spectral Clustering and the Graph Laplacian**, *Networks Reading Group, RISE Lab, IIT Madras*
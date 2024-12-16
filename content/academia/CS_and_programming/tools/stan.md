---
title: "Stan"
date: 2024-12-15T14:10:43+01:00
draft: false
---

Stan is a software tool for Bayesian statistics inference and much more. 

Like many others, I have become an evangelist of Stan, for several reasons:
  - it's simply, in my humble opinion the better way of doing statistics, as this approach more or less forces you to think generatively, but also that it will provide you with the entire distribution and its properties in stead of only estimates. 
  - it's flexible in the sense that it will accommodate most needs of the far majority of tasks you throw at it. 
  - It's physics-informed; the NUTS-sampler is inspired by physics and implemented using symplectic integrators, ensuring the quality of the inference (given reasonable input of course). 
  - it's responsive! It will tell you that the output is probably nonsense if you feed it nonsense
  - It's well integrated as a standard for frameworks of Bayesian inference which means that many programming languages have at the very least an API to call a STAN back-end. 
    
While there is no such thing as a perfect piece of software, Stan is awesome!
Problems will of course occur, but so will the solutions to those problems!
If it is not described in the documentation [here](https://mc-stan.org/users/documentation/) you can probably find it on the blogs of either [Michael Betancourt](https://betanalpha.github.io/) or [Andrew Gelman](https://statmodeling.stat.columbia.edu/)
The community using Stan is extremely broad in academic background, and very active in problem-solving with Stan and the further development of the language/tool. 

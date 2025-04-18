---
title: "Multiindex_arviz"
date: 2025-04-16T13:00:41+02:00
draft: true
---

OK, so you have made a hierarchical model in STAN, and you want to visualize the results of the sampling, using Arviz in Python. 

Turns out this was unexpectedly hard, because of the implementation of the model:
A single index running over multiple instances/sub-levels in the model. 

So you are left with the choice of plotting everything at once, but you want to make selections based on the sub-levels. 

This can be achieved with adding an index along the naive data-index, marking the hierarchical structure. 

This(as far as i know) is not possible in Arviz natively, but possible using the underlying `xarray` structures and methods native the groups in Arviz inference data tree/object. 

To make this concrete, let us explore the Iris dataset again:




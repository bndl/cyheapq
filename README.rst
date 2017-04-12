=========================
CyHeapQ - HeapQ in Cython
=========================

This module is an adaptation of merge, nlargest and nsmallest from the heapq module in Cython. This
makes it just a tad bit faster.

x 1.5 for nlargest and nsmallest (given a particular micro benchnmark of course). x 3 for merge.
nlargest performance is comparable with cytoolz.topk (but cyheapq also provides nsmallest). merge
is around 8 times faster than cytoolz.merge_sorted. The microbenchmark used involves sifting /
merging 10e6 random floats.

---
title: Subtle Bugs
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/subtle-bugs.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:56f4b3e1dc920437'
translated: false
---

> 原文：[Subtle Bugs](https://www.mikeash.com/pyblog/subtle-bugs.html)　·　mikeash.com Friday Q&A

Posted at 2007-07-10 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Performance Comparisons of Common Operations](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html)  
Previous article: [Open Source](https://www.mikeash.com/pyblog/open-source.html)  
Tags: [chemicalburn](https://www.mikeash.com/pyblog/?tag=chemicalburn) [debugging](https://www.mikeash.com/pyblog/?tag=debugging)

Subtle Bugs

by [Mike Ash](https://www.mikeash.com/)

First some background. ChemicalBurn is a realtime showcase of [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra) as well as self-organizing networks. The presentation consists of a number of nodes, somewhere between 5 and 500 but usually 50-200, connections between those nodes which are weighted depending on how much traffic they carry, and packages which are generated at nodes and flow through the network to their destinations. Depending on the settings, nodes will be created and destroyed at random, adjusting the network as appropriate. When a node is destroyed, it's first marked for destruction but not removed. Only when all traffic to it has ceased will it be taken out of the network.  
   
 One bug was an interesting case where the screensaver would simply freeze up when run with a very small number of nodes. It doesn't occur with larger numbers of nodes so I hadn't seen any reports on it, but it showed up in my testing. It would run for a few seconds then freeze, stuck in an endless routing loop.  
   
 It was pretty easy to track down since it would freeze quickly and reliably. Some poking around in the debugger revealed that the freeze was always associated with a destination node which had a small number of connections. This was weird because in ChemicalBurn, all nodes are supposed to have connections to all other nodes. A small number of connections should never be able to happen.  
   
 The bug in this case turned out to be in my node generating code. When a new node is created it's connected to all existing nodes. The bug was that connections were only generated to live nodes, but not to dying nodes. With the small number of nodes there was a lot of creation and destruction going on, and with this bug it was possible to have the network split into two completely disconnected pieces. When a package tried to route from one half to the other, the routing algorithm wedged. The fix was easy: generate connections from new nodes to dying nodes.  
   
 The much nastier bug was hitting some users much more than others, and of course it only hit me rarely. I couldn't find a pattern to it, but it seemed like it might be hardware related. I suspected a bug in my threading code. The problem would manifest with the routing algorithm failing to find a path to a package's destination, which then caused the screensaver to die. It only happened rarely, every 15-30 minutes at best and never at worst, so I had a hard time making it happen so I could debug it.  
   
 I disabled the graphics and the framerate limiter so I could try to force the problem as quickly as possible. With some experimentation I was able to find settings that would cause it to happen after 5-10 minutes. Poking in the debugger revealed that the package was attempting to reach a node which no longer existed. This obviously confused the routing algorithm to the point of destruction. But this should never happen: packages can only have existing nodes as their destinations, and when a node is destroyed, packages with that node as their destination are rerouted to a random live node.  
   
 I added more and more debug logging so I could go back and trace what happened before the crash, since the program state at the time of the crash wasn't very illuminating. One run generated 98MB of logs and I finally found the problem.  
   
 Above, I said that when a node is marked for removal, packages are rerouted away from it. This is not quite complete. Packages which are on a connection leading to the node are not rerouted, with the idea that it's faster for them to finish their journey than to go somewhere else.  
   
 The problem is that this code didn't check the _direction_ of travel along the connection. It is possible, though rare, for a package to be on such a connection but moving _away_ from its destination node. This would happen if the node had already been rerouted once, and by coincidence it was rerouted to the node it had just come from.  
   
 But this isn't enough to trigger the problem. Nodes marked for removal are finally removed when they have no more packages on their connections. The package in question has to be routed off its connection and onto a prospective shorter path. While it's away from its destination node all of the other packages on its connections have to go elsewhere too. Once the node's connections are clear, it will be removed, and the package in question will trigger a routing crash next time it hits a node. If the package isn't rerouted just so, or if it returns on the connection it came from, or if other packages occupy the destination node long enough to keep it alive until this package can make it back onto a connection headed for it, then the crash won't happen.  
   
 Having finally deduced all of this, the fix was simple: only packages on a connection to the targeted node and _moving in the right direction_ are left alone, and all other packages, including ones on these connections but moving away, are redirected. And just like that, no more crashes.  
   
 The biggest surprise to me is that this wasn't related to the multithreading code. Multithreading is hard and prone to weird bugs like this, and I only started hearing about this problem after I added it, so I was pretty sure that would be the cause.  
   
 The big lessons learned here are the usual ones. First, think about the constraints you set on your data, then make sure your code maintains them. In this case, one constraint was that the graph is fully connected, but my code was not fully connecting new nodes. Second, challenge your assumptions. Here, my code assumed that a package that was on a connection which led to its destination was moving in the direction of its destination, but in fact it was possible due to dynamic rerouting for it to be moving in the opposite direction, which really broke my code. This was very hard to think of beforehan, but it's possible if I had been thinking in a really paranoid manner I might have constrained the test properly even without knowing why, just in the spirit of being cautious.

**No comments:**

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/subtle-bugs.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

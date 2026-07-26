---
title: 'Friday Q&A 2009-04-10: Multithreaded Optimization in ChemicalBurn'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-04-10-multithreaded-optimization-in-chemicalburn.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6d95bb4add8cf151'
translated: false
---

> 原文：[Friday Q&A 2009-04-10: Multithreaded Optimization in ChemicalBurn](https://www.mikeash.com/pyblog/friday-qa-2009-04-10-multithreaded-optimization-in-chemicalburn.html)　·　mikeash.com Friday Q&A

Posted at 2009-04-10 17:22 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-04-17: Code Generation with LLVM, Part 1: Basics](https://www.mikeash.com/pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)  
Previous article: [Friday Q&A 2009-04-03: On Hold](https://www.mikeash.com/pyblog/friday-qa-2009-04-03-on-hold.html)  
Tags: [chemicalburn](https://www.mikeash.com/pyblog/?tag=chemicalburn) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [performance](https://www.mikeash.com/pyblog/?tag=performance) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2009-04-10: Multithreaded Optimization in ChemicalBurn

by [Mike Ash](https://www.mikeash.com/)

**Background**

If you aren't familiar with [ChemicalBurn](http://www.mikeash.com/?page=software/chemicalburn/), you should go check it out. Essentially, it shows a network with packages being routed through the network. The trick is that the network's performance is changed by the packages as they move, leading to an interesting dynamic system.

If you would like to follow along, the [source code](http://www.mikeash.com/svn/ChemicalBurn/) is also available.

The core of ChemicalBurn is the routing algorithm. At each time step, packages are generated within the system. They're given a random source and a random destination. Given all of the connections and their speeds, the system computes the optimal route. Since the connections can change at any moment, this routing is redone every time the package arrives at an intermediate node. With simple OpenGL graphics and not much else going on, the routing algorithm is easily the bottleneck of the entire screensaver.

**Algorithm**  
 The routing method is located in [ChemicalBurnView](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnView.m). It's a bit messy owing to its heavy optimization, but it's just an implementation of the standard route finding algorithm, [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm). (For all of you jumping up and down in the back yelling about [A*](http://en.wikipedia.org/wiki/A*_search_algorithm), ChemicalBurn is not well suited to A* due to the lack of a good heuristic.)

Follow the links for the full explanation, but the basics of this algorithm are really simple. Each node in the graph gets a cost and a predecessor. Keep a queue of nodes, initialized with the starting node. In a loop, pop the node with the cheapest cost from the queue. Enumerate through all of its connections. If the cost of getting to that node, plus the cost of the connection, is cheaper than the current cost set on that other node, set that node's cost to the sum, and set its predecessor to the node that was just popped. Once you pop the destination node, follow the predecessor links back and you have the cheapest path to the destination.

**Priority Queue**  
 The heart of this algorithm is the queue of pending nodes. My initial implementation simply stored them in an NSMutableSet. To fetch the cheapest one, I simply iterated through the set and looked for the the one with the lowest cost. This queue can get pretty big, and since this search happens every time through the inner loop of this screensaver's major hotspot, this was really slow.

The easy answer here was to switch to using a priority queue. If you aren't familair, this is a specialized data structure which efficiently supports adding arbitrary elements and fetching the "smallest" element according to some arbitrary test. I chose to write [a wrapper](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnOrderedQueue.mm) around the C++ STL's heap algorithm. Another good choice for this would be the [CFBinaryHeap](http://developer.apple.com/documentation/CoreFOundation/Reference/CFBinaryHeapRef/index.html) class available in CoreFoundation. This one change gave a hefty speedup.

**Inline Metadata**  
 The routing algorithm depends on having two pieces of metadata for each node. Originally, I implemented this by using two CFMutableDictionary instances that used the nodes for keys and had the cost and back pointer as values. But since these values were constantly being fetched and set inside of this very hot loop, even the normally fast dictionary lookups were getting to be slow. The solution to this was easy, and is actually a common way to implement Dijkstra's algorithm: store these two values in the nodes themselves. I just made them public instance variables, and my slow dictionary lookups were transformed to fast ivar lookups.

**Multithreading**  
 Since each package's routing is independent of the others, and since many packages needed to be routed for each frame in the compute-bound case, multithreading the route finding code was an obvious way to gain more speed.

How I implemented the multithreading itself is not all that interesting. I took an obvious and standard approach of spawning as many worker threads as the machine has processor cores, then pushing packages into a queue which the worker threads access.

There's a hitch, though. I said that each package's routing is independent of the others, but that's not true. In the original implementation it was, but the **inline metadata** optimization screws this up. The per-node values are conceptually private to each individual routing problem, but storing them in instance variables makes them globally visible, so the worker threads are bound to fight over them.

The trick to solving this problem was to store not just a single pair of values, but to store an array of values. The [ChemicalBurnNode](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnNode.h) class ended up looking like this:

```
    @class ChemicalBurnNode;
    struct ChemicalBurnNodePerThread {
        unsigned             cost;
        ChemicalBurnNode*    prev;
    };
    
    @interface ChemicalBurnNode : NSObject {
        unsigned             mID;
        NSPoint              mPos;
        
        @public
        struct ChemicalBurnNodePerThread    mPerThread[0];
    }
```

That `[0]` is a trick to implement a variable-length array. I didn't want to hardcode a value for the maximum number of threads, and then have some huge multi-core beast come along in a few years and not be able to take advantage. To set up the storage for the array, I override `+allocWithZone:` in [the implementation](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnNode.m) to allocate some extra space:

```
+ allocWithZone: (NSZone *)zone
    {
        unsigned extraBytes = gProcessorCount * sizeof( struct ChemicalBurnNodePerThread );
        return NSAllocateObject( self, extraBytes, zone );
    }
```

That solves the problem of storage, but leaves the problem of how to choose an array index. Obviously each thread needs to choose a different one. And obviously each thread needs to choose a small number.

I wrote a pair of functions for this:

```
    // the key parameter allows multiple independent views to share IDs
    // IDs will count up from 0 based on the unique key passed in
    int NodeGetThreadID( void *key );
    void NodeThreadIDCleanup( void *key );
```

The idea being that as different threads call `NodeGetThreadID`, the returned value starts at 0 and just increments for each new thread that appears. This is accomplished by using `pthread_getspecific` to store the ID per-thread, and using a [CFBag](http://developer.apple.com/DOCUMENTATION/CoreFoundation/Reference/CFBagRef/index.html) to keep track of how many threads have already requested IDs for the given key, so that each new thread gets the appropriate ID. Here's how they're implemented:

```
    int NodeGetThreadID( void *key )
    {
        // we store ID + 1 because NULL is used to indicate "does not exist"
        int threadID = (int)pthread_getspecific( gThreadIDKey );
        if( threadID == 0 )
        {
            pthread_mutex_lock( &gIDMutex );
            CFBagAddValue( gIDs, key );
            threadID = CFBagGetCountOfValue( gIDs, key );
            pthread_mutex_unlock( &gIDMutex );
            
            pthread_setspecific( gThreadIDKey, (void *)threadID );
            
            if( threadID > gProcessorCount )
                NSLog( @"Attempted to get ID for thread #%d, more than allowed!", threadID );
        }
        
        return threadID - 1;
    }
    
    static void MakeKey( void )
    {
        int err = pthread_key_create( &gThreadIDKey;, NULL );
        if( err )
            NSLog( @"%s: pthread_key_create returned %d", __func__, err );
    }
    
    void NodeThreadIDCleanup( void *key )
    {
        while( CFBagGetCountOfValue( gIDs, key ) )
            CFBagRemoveValue( gIDs, key );
    }
```

(The `MakeKey` function is just called once from the class's `+initialize` method.)

And that's all it took to get this code to play nice with multiple worker threads but still allow fast access to the two critical pieces of node metadata.

**Conclusion**  
 It's been a long time since I worked on ChemicalBurn, but my recollection is that all of these optimizations put together resulted in something like a 100x speedup from start to finish on my 4-core Mac Pro.

All of these optimizations were relatively obvious and straightforward, but they were also extremely effective. There's a nice combination of optimization techniques here. Using a priority queue instead of a set made a huge difference in the algorithm's overall performance, since the priority queue has an `O(log n)` running time instead of the `O(n)` of the set. Moving the node metadata to be ivars of the node objects is a pure micro-optimization, but one which yielded significant benefits due to how often that particular data was accessed. And then multithreading the routing code is an obvious way to use parallel computing to good advantage.

That wraps up this week's Friday Q&A. Come back next week, when hopefully the surfeit of wiener dogs which prevented me from producing last week's post will keep out of my way once again and I can talk about another reader-contributed topic. Remember, Friday Q&A is powered by your ideas. If you have a question or a topic that you would like to see discussed, post it in the comments or [e-mail it to me](mailto:mike@mikeash.com) (tell me if you don't want me to use yoru name).

Have a question or comment about this code? Want to tell your own optimization war story? Post your comments below.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).

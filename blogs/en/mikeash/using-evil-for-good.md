---
title: Using Evil for Good
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/using-evil-for-good.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:04b3bceef45ef7b4'
translated: false
---

> 原文：[Using Evil for Good](https://www.mikeash.com/pyblog/using-evil-for-good.html)　·　mikeash.com Friday Q&A

Posted at 2006-07-14 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Getting Answers](https://www.mikeash.com/pyblog/getting-answers.html)  
Previous article: [Autorelease is Fast](https://www.mikeash.com/pyblog/autorelease-is-fast.html)  
Tags: [c++](https://www.mikeash.com/pyblog/?tag=c%2B%2B) [chemicalburn](https://www.mikeash.com/pyblog/?tag=chemicalburn) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [stl](https://www.mikeash.com/pyblog/?tag=stl)

Using Evil for Good

by [Mike Ash](https://www.mikeash.com/)

I've been quoted as saying things such as:

> ObjC++ also allows you to create an incredible menagerie of abominations such as the world has never seen

Indeed, I shudder every time I think about the autoptr/autorelease or exceptions conversion wrappers I've seen people construct. On the other hand, C++ does have a lot of [fast, standard data structures](http://www.sgi.com/tech/stl/).

Ordinarily I don't sympathize much with people who complain about Cocoa lacking data structures. It's true that having nothing but [arrays"](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/Reference/Reference.html), [sets](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSSet_Class/Reference/Reference.html), and [dictionaries](https://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSDictionary_Class/Reference/Reference.html) can be a bit limiting at times. On the other hand, people who complain about the limited choice tend to be complaining for its own sake, and don't have any actual need for other things.

And really, you can press these things into service reasonably well in place of other data structures. NSMutableArray makes for a fine stack and a decent (if slowish) queue, and NSDictionary and NSSet take care of many of the things that a tree structure would be used for in other languages.

But sometimes you just need something better. [ChemicalBurn](http://www.mikeash.com/?page=software/chemicalburn/index.html) 1.0 is about ten times faster than the first working version I produced that I deemed acceptable. A good chunk of the optimization was giving up Cocoa drawing and moving to OpenGL. Once that was done, I profiled the app and noticed that it was spending approximately all of its time doing route finding.

As we all know, the best optimizations are algorithmic improvements. If you have a reasonably large data set, all the low-level diddling in the world won't save you as much as switching from an O(n^5) to an O(n^3) algorithm.

ChemicalBurn uses [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to perform pathfinding. It's a fairly straightforward algorithm. Basically, you brute-force all of the connections, but do it in a clever way so that you can stop your search early.

One of the key structures used in this algorithm is the set of all untraversed nodes. Every time through the algorithm's outer loop, the node with the lowest cost is removed from that set and examined. If that node is your destination then your work is complete, otherwise you use that node to update the cost of all the other nodes.

The simple implementation of that set is to just keep all of the nodes in no particular order. Then you can scan them all and pick out the smallest one. This takes O(n). In the worst case this is done n times, once per node, and then in each node we need to perform n-1 operations in order to compare the cost of connecting to every other node in the graph. This makes the final performance O(n^3), which is not so great.

The obvious fix for this is to use a priority queue for the set of untraversed nodes. This changes selection from O(n) to O(lg n), making the entire algorithm run at O(n^2 lg n), a clear improvement.

But, oops, Cocoa doesn't have a priority queue. I went hunting around for an implementation but I couldn't find a decent one, and I didn't feel like writing one myself. Finally, I realized that [STL](http://www.sgi.com/tech/stl) probably had one, so I looked it up and sure enough, it does. And better yet, it has priority queue algorithms that work on plain C arrays, so I could wrap a Cocoa class around a plain C array and dump in the STL algorithms and I'm all set.

Without further ado, here's my (short) implementation of the wrapper. You may use it at will in any place and for any purpose which does not involve radioactive monkeys. Oh, and don't ask me why I called it an OrderedQueue instead of a PriorityQueue or a Heap, I really couldn't tell you:

```
// .h
@interface ChemicalBurnOrderedQueue : NSObject {
	struct CBOQNode*	mObjs;
	unsigned			mCount;
	unsigned			mCapacity;
	
	BOOL				mHeapified;
}

- init;

- (unsigned)count;
- (void)addObject: (id)obj value: (unsigned)val;
- (id)pop;

@end

// .m
#import 

struct CBOQNode {
	id obj;
	unsigned val;
};

static bool NodeLessThan( struct CBOQNode &n1;, struct CBOQNode &n2; )
{
	if( n1.val != n2.val )
		return n1.val > n2.val;
	else
		return (unsigned)n1.obj < (unsigned)n2.obj;
}

@implementation ChemicalBurnOrderedQueue

- init
{
	if( ( self = [super init] ) )
	{
		mCount = 0;
		mCapacity = 100;
		mObjs = (struct CBOQNode *)malloc( mCapacity * sizeof( *mObjs ) );
	}
	return self;
}

- (void)dealloc
{
	free( mObjs );
	
	[super dealloc];
}

#pragma mark -

- (void)buildheap
{
	std::make_heap( mObjs, mObjs + mCount, NodeLessThan );
	mHeapified = YES;
}

#pragma mark -

- (unsigned)count
{
	return mCount;
}

- (void)addObject: (id)obj value: (unsigned)val
{
	mCount++;
	if( mCount > mCapacity )
	{
		mCapacity *= 2;
		mObjs = (struct CBOQNode *)realloc( mObjs, mCapacity * sizeof( *mObjs ) );
	}
	
	mObjs[mCount - 1].obj = obj;
	mObjs[mCount - 1].val = val;
	
	if( mHeapified )
		std::push_heap( mObjs, mObjs + mCount, NodeLessThan );
}

- (id)pop
{
	if( !mHeapified )
	{
		[self buildheap];
	}
	
	std::pop_heap( mObjs, mObjs + mCount, NodeLessThan );
	mCount--;
	return mObjs[mCount].obj;
}

- (NSString *)description
{
	NSMutableString *str = [NSMutableString string];
	
	[str appendString: @"ChemicalBurnOrderedQueue = (n"];
	unsigned i;
	for( i = 0; i < mCount; i++ )
		[str appendFormat: @"t%@ = %un", mObjs[i].obj, mObjs[i].val];
	[str appendString: @")n"];
	
	return str;
}

@end
```

And so there you have it. It's delightfully simple with STL doing the heavy lifting, and it sped ChemicalBurn up by around a factor of two with no other changes. Not bad for something this simple!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/using-evil-for-good.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

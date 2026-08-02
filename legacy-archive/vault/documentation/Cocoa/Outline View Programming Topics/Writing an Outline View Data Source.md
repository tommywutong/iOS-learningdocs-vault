---
title: Outline View Programming Topics
apple_id: 10000023i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OutlineView/Articles/UsingOutlineDataSource.html
archived_at: '2026-07-15T07:17:39.573520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Outline View Programming Topics](Introduction%20to%20Outline%20Views.md)


[Next](Using%20an%20Outline%20View%20Delegate.md)[Previous](About%20Outline%20Views.md)

# Writing an Outline View Data Source

Outline views support a data-source delegate in addition to a standard delegate object. The data-source implements the [NSOutlineViewDelegate](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate) protocol and provides data and information about that data to the outline view, and is responsible for managing the data. Although an outline view does not require a delegate, it must have a data source to display information.

Like an instance of `NSTableView`, an instance of `NSOutlineView` gets all of its data from an object that you provide, called its data source. Your data source object can store records in any way you choose, but it must be able to identify them by their position in the hierarchy through the [NSOutlineViewDataSource](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource) protocol (prior to OS X v10.6, this was an informal protocol—`NSOutlineViewDataSource`). The data source must minimally implement the data access methods ([outlineView:child:ofItem:](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1528977-outlineview), [outlineView:isItemExpandable:](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535198-outlineview), [outlineView:numberOfChildrenOfItem:](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535549-outlineview), and [outlineView:objectValueForTableColumn:byItem:](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1531606-outlineview)). To specify the root item in any of these methods, `nil` is sent as the method’s _item_ argument. If you want to allow the user to edit items, you must also implement a method for changing the value of an attribute ([outlineView:setObject:forTableColumn:byItem:](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1534817-outlineview)).

Typically the data source itself manages a collection of model objects each of which knows what their value is, whether they represent a leaf node, and how many (if any) child objects they have.

Just like a table view, an outline view uses the data source solely to get information. An outline view does not own its data source. Similarly, it does not own the objects it gets from the data source—if they are released your application is likely to crash unless you tell the outline view to reload its data.

The data source is a controller object, and you are responsible for ensuring that it is not deallocated before the outline view is finished with it (typically the data source is an object such as the document object in a document-based application, so there is no additional work to do). The data source is in turn responsible for retaining all of the objects it provides to an outline view, and updating the outline view when there’s a change to the model. It is therefore not safe to release the root item—or any children—until you’re no longer displaying it in the outline view. If you need to dispose of the root item, then you should ensure that references to it are nullified, and that the outline view is updated to ensure that no attempt is made to display other items that may also have been disposed of, as in the following example.

```
    [rootItem release];
    rootItem = nil;
    [outlineView reloadData];
```


The following example shows the implementation of a data source class used in conjunction with an outline view to display contents of the file system, and of a class used to represent entries in the file system. Listing 1 shows the implementation of the data source class. Listing 2 shows the implementation of a class used to represent entries in the file system. The singleton `rootItem` instance is used as the root object in the example in Listing 1.

__Listing 1__  Implementation of Outline View Data Source

```objc
@implementation DataSource
// Data Source methods

- (NSInteger)outlineView:(NSOutlineView *)outlineView numberOfChildrenOfItem:(id)item {

    return (item == nil) ? 1 : [item numberOfChildren];
}


- (BOOL)outlineView:(NSOutlineView *)outlineView isItemExpandable:(id)item {
    return (item == nil) ? YES : ([item numberOfChildren] != -1);
}


- (id)outlineView:(NSOutlineView *)outlineView child:(NSInteger)index ofItem:(id)item {

    return (item == nil) ? [FileSystemItem rootItem] : [(FileSystemItem *)item childAtIndex:index];
}


- (id)outlineView:(NSOutlineView *)outlineView objectValueForTableColumn:(NSTableColumn *)tableColumn byItem:(id)item {
    return (item == nil) ? @"/" : [item relativePath];
}

@end
```


__Listing 2__  Implementation of Outline View Data Source Item

```objc
@interface FileSystemItem : NSObject
{
    NSString *relativePath;
    FileSystemItem *parent;
    NSMutableArray *children;
}

+ (FileSystemItem *)rootItem;
- (NSInteger)numberOfChildren;// Returns -1 for leaf nodes
- (FileSystemItem *)childAtIndex:(NSUInteger)n; // Invalid to call on leaf nodes
- (NSString *)fullPath;
- (NSString *)relativePath;

@end


@implementation FileSystemItem

static FileSystemItem *rootItem = nil;
static NSMutableArray *leafNode = nil;

+ (void)initialize {
    if (self == [FileSystemItem class]) {
        leafNode = [[NSMutableArray alloc] init];
    }
}

- (id)initWithPath:(NSString *)path parent:(FileSystemItem *)parentItem {
    self = [super init];
    if (self) {
       relativePath = [[path lastPathComponent] copy];
       parent = parentItem;
       }
    return self;
}


+ (FileSystemItem *)rootItem {
    if (rootItem == nil) {
        rootItem = [[FileSystemItem alloc] initWithPath:@"/" parent:nil];
    }
    return rootItem;
}


// Creates, caches, and returns the array of children
// Loads children incrementally
- (NSArray *)children {

    if (children == nil) {
        NSFileManager *fileManager = [NSFileManager defaultManager];
        NSString *fullPath = [self fullPath];
        BOOL isDir, valid;

        valid = [fileManager fileExistsAtPath:fullPath isDirectory:&isDir];

        if (valid && isDir) {
            NSArray *array = [fileManager contentsOfDirectoryAtPath:fullPath error:NULL];

            NSUInteger numChildren, i;

            numChildren = [array count];
            children = [[NSMutableArray alloc] initWithCapacity:numChildren];

            for (i = 0; i < numChildren; i++)
            {
                FileSystemItem *newChild = [[FileSystemItem alloc]
                                   initWithPath:[array objectAtIndex:i] parent:self];
                [children addObject:newChild];
                [newChild release];
            }
        }
        else {
            children = leafNode;
        }
    }
    return children;
}


- (NSString *)relativePath {
    return relativePath;
}


- (NSString *)fullPath {
    // If no parent, return our own relative path
    if (parent == nil) {
        return relativePath;
    }

    // recurse up the hierarchy, prepending each parent’s path
    return [[parent fullPath] stringByAppendingPathComponent:relativePath];
}


- (FileSystemItem *)childAtIndex:(NSUInteger)n {
    return [[self children] objectAtIndex:n];
}


- (NSInteger)numberOfChildren {
    NSArray *tmp = [self children];
    return (tmp == leafNode) ? (-1) : [tmp count];
}


- (void)dealloc {
    if (children != leafNode) {
        [children release];
    }
    [relativePath release];
    [super dealloc];
}

@end
```

[Next](Using%20an%20Outline%20View%20Delegate.md)[Previous](About%20Outline%20Views.md)


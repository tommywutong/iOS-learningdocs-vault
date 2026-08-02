---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DetectChange.html
archived_at: '2026-07-15T08:01:04.976175Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Detecting Changed Attributes

##  Synopsis

Describes how to find out what attributes have changed in an object before those changes are committed.

##  Description

By default, before an enterprise object modifies its state, it sends itself a _willChange_
message which, in turn, causes the _objectWillChange_
notification to be sent to all registered observers, particularly the object's editing context. In response, the editing context records a snapshot of the object's state before the modification takes place, allowing later comparisons against the modified object to determine precisely which modifications were made. However, the _objectWillChange_
notification is generic and does not specify the attribute of the object that is to be changed.

With a simple technique, you can determine which attributes of an object have changed before these changes are committed to the database. First, as delegate of EOEditing context, implement a suitable delegate method such as _editingContextWillSaveChanges_
. In this method, assuming that your Enterprise Object descends either from NSObject (in Objective-C) or from the EOCustomObject class in Java, you can first determine the original snapshot using the following EOEditingContext method:

#####  Figure 1. Objective-C Code

```objc
- (NSDictionary *)committedSnapshotForObject:(id)object;
```


#####  Figure 2. Java Code

```
public native com.apple.yellow.foundation.NSDictionary committedSnapshotForObject (com.apple.yellow.eocontrol.EOEnterpriseObject);
```


You can next get all the changes to the object's original snapshot.

#####  Figure 3. Objective-C

```objc
- (NSDictionary *)changesFromSnapshot:(NSDictionary *)snapshot;
```


#####  Figure 4. Java Code

```
public native com.apple.yellow.foundation.NSDictionary changesFromSnapshot (com.apple.yellow.foundation.NSDictionary);
```


The NSDictionary object returned from the _changesFromSnapshot_
method (in both languages) only contains the attribute names and their values that refer to uncommitted changes in the object. If there is a to-many attribute, the uncommitted value is an array of two arrays: uncommitted additions and uncommitted deletions.

The following Java sample code gets the NSDictionaries reflecting the prior committed state of an object and its currently changed attributes, based on the API described above:

#####  Figure 5. Java Code

```
/* Assuming that myCustomObject descends from EOCustomObject and already exists */
```



```
EOEditingContext ec = myCustomObject.editingContext();
```



```
// The committedSnapshotForObject method expects to have
```



```
// an EOEnterpriseObject as argument, so typecasting is necessary here.
```



```
NSDictionary  originalSnapshot = ec.committedSnapshotForObject((EOEnterpriseObject)myCustomObject);
```



```
NSDictionary changesDict = myCustomObject.changesFromSnapshot(originalSnapshot);
```


To view all changes recorded in the changed snapshot, you could use the following sample code:

#####  Figure 6. Java Code

```
int count;
```



```
count = changesDict.count();
```



```
NSArray allKeys = changesDict.allKeys();
```



```
java.util.Enumerator anEnum = changesDict.keyEnumerator();
```



```
while (anEnum.hasMoreElements()) {
```



```
\xA0\xA0\xA0\xA0String key = anEnum.nextElement();
```



```
\xA0\xA0\xA0\xA0String value = changesDict.valueForKey(key);
```



```
\xA0\xA0\xA0\xA0System.out.println("Changes: Key "
```



```
     + key + "Value "
```



```
    + value);
```



```
}
```


##  See Also

· Saving

##  Questions

· How do I determine which attributes have been modified before committing them to the database?

##  Keywords

· Saving Changes

· EOCustomObject

· snapshot

· Changed Attributes

· Committing Changes

##  Revision History

14 July, 1998. Mai Nguyen. First Draft.

17 November, 1998. Terry Donoghue. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

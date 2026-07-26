---
title: Publisher Operators
framework: Combine
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/just-publisher-operators
source_url: 'https://developer.apple.com/documentation/combine/just-publisher-operators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just-publisher-operators.json'
content_hash: 'sha256:7515030929d7f9eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md) · [Just](just.md)

# Publisher Operators

<sub>API Collection</sub>

Methods that create downstream publishers or subscribers to act on the elements they receive.

## Topics

### Mapping elements

- [map(_:)](<just/map(__).md>)
- [tryMap(_:)](<just/trymap(__).md>)
- [mapError(_:)](<just/maperror(__).md>)
- [scan(_:_:)](<just/scan(____).md>)
- [tryScan(_:_:)](<just/tryscan(____).md>)
- [setFailureType(to:)](<just/setfailuretype(to_).md>)

### Filtering elements

- [filter(_:)](<just/filter(__).md>)
- [compactMap(_:)](<just/compactmap(__).md>)
- [removeDuplicates()](<just/removeduplicates().md>)
- [removeDuplicates(by:)](<just/removeduplicates(by_).md>)
- [tryRemoveDuplicates(by:)](<just/tryremoveduplicates(by_).md>)
- [replaceEmpty(with:)](<just/replaceempty(with_).md>)
- [replaceError(with:)](<just/replaceerror(with_).md>)

### Reducing elements

- [collect()](<just/collect().md>)
- [ignoreOutput()](<just/ignoreoutput().md>)
- [reduce(_:_:)](<just/reduce(____).md>)
- [tryReduce(_:_:)](<just/tryreduce(____).md>)

### Applying mathematical operations on elements

- [count()](<just/count().md>)
- [max()](<just/max().md>)
- [max(by:)](<just/max(by_).md>)
- [min()](<just/min().md>)
- [min(by:)](<just/min(by_).md>)

### Applying matching criteria to elements

- [contains(_:)](<just/contains(__).md>)
- [contains(where:)](<just/contains(where_).md>)
- [tryContains(where:)](<just/trycontains(where_).md>)
- [allSatisfy(_:)](<just/allsatisfy(__).md>)
- [tryAllSatisfy(_:)](<just/tryallsatisfy(__).md>)

### Applying sequence operations to elements

- [dropFirst(_:)](<just/dropfirst(__).md>)
- [drop(while:)](<just/drop(while_).md>)
- [append(_:)](<just/append(__)-7eyqj.md>)
- [append(_:)](<just/append(__)-7sxlu.md>)
- [prepend(_:)](<just/prepend(__)-39e57.md>)
- [prepend(_:)](<just/prepend(__)-7fg73.md>)
- [prefix(_:)](<just/prefix(__).md>)
- [prefix(while:)](<just/prefix(while_).md>)

### Selecting specific elements

- [first()](<just/first().md>)
- [first(where:)](<just/first(where_).md>)
- [last()](<just/last().md>)
- [last(where:)](<just/last(where_).md>)
- [output(at:)](<just/output(at_).md>)
- [output(in:)](<just/output(in_).md>)

### Handling errors

- [retry(_:)](<just/retry(__).md>)

---
title: Deprecated Symbols
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/deprecated-symbols
source_url: 'https://developer.apple.com/documentation/objectivec/deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/deprecated-symbols.json'
content_hash: 'sha256:c53fee4ba25eb543'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# Deprecated Symbols

<sub>API Collection</sub>

Review symbols that are no longer supported and find the replacements to use instead.

## Topics

### Deprecated Class Methods

- [+ defaultPlaceholderForMarker:withBinding:](<nsobject-swift.class/defaultplaceholder(for_with_).md>) — Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ setDefaultPlaceholder:forMarker:withBinding:](<nsobject-swift.class/setdefaultplaceholder(__for_with_).md>) — Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ useStoredAccessor](<nsobject-swift.class/usestoredaccessor().md>) — Returns `true` if the stored value methods [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors. _(deprecated)_

### Deprecated Methods

- [- accessibilityAttributeNames](<nsobject-swift.class/accessibilityattributenames().md>) — Returns an array of attribute names supported by the receiver. _(deprecated)_
- [- accessibilityAttributeValue:](<nsobject-swift.class/accessibilityattributevalue(__).md>) — Returns the value of the specified attribute in the receiver. _(deprecated)_
- [- accessibilityAttributeValue:forParameter:](<nsobject-swift.class/accessibilityattributevalue(__forparameter_).md>) — Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter. _(deprecated)_
- [- accessibilityActionDescription:](<nsobject-swift.class/accessibilityactiondescription(__).md>) — Returns a localized description of the specified action. _(deprecated)_
- [- accessibilityActionNames](<nsobject-swift.class/accessibilityactionnames().md>) — Returns an array of action names supported by the accessibility element. _(deprecated)_
- [- accessibilityArrayAttributeCount:](<nsobject-swift.class/accessibilityarrayattributecount(__).md>) — Returns the count of the specified accessibility array attribute. _(deprecated)_
- [- accessibilityArrayAttributeValues:index:maxCount:](<nsobject-swift.class/accessibilityarrayattributevalues(__index_maxcount_).md>) — Returns a subarray of values of an accessibility array attribute. _(deprecated)_
- [- accessibilityIndexOfChild:](<nsobject-swift.class/accessibilityindex(ofchild_).md>) — Returns the index of the specified accessibility child in the parent. _(deprecated)_
- [- accessibilityIsAttributeSettable:](<nsobject-swift.class/accessibilityisattributesettable(__).md>) — Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set. _(deprecated)_
- [- accessibilityIsIgnored](<nsobject-swift.class/accessibilityisignored().md>) — Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy. _(deprecated)_
- [- accessibilityParameterizedAttributeNames](<nsobject-swift.class/accessibilityparameterizedattributenames().md>) — Returns a list of parameterized attribute names supported by the receiver. _(deprecated)_
- [- accessibilityPerformAction:](<nsobject-swift.class/accessibilityperformaction(__).md>) — Performs the action associated with the specified action. _(deprecated)_
- [- accessibilitySetOverrideValue:forAttribute:](<nsobject-swift.class/accessibilitysetoverridevalue(__forattribute_).md>) — Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value. _(deprecated)_
- [- accessibilitySetValue:forAttribute:](<nsobject-swift.class/accessibilitysetvalue(__forattribute_).md>) — Sets the value of the specified attribute in the receiver to the specified value. _(deprecated)_
- [- fileManager:shouldProceedAfterError:](<nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [- fileManager:willProcessPath:](<nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [- finalize](<nsobject-swift.class/finalize().md>) — The garbage collector invokes this method on the receiver before disposing of the memory it uses. _(deprecated)_
- [- fontManager:willIncludeFont:](<nsobject-swift.class/fontmanager(__willincludefont_).md>) — Requests permission from the Font panel delegate to display the given font name in the Font panel. _(deprecated)_
- [- namesOfPromisedFilesDroppedAtDestination:](<nsobject-swift.class/namesofpromisedfilesdropped(atdestination_).md>) — Returns the names of the files that the receiver promises to create at a specified location. _(deprecated)_
- [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) — Returns the property identified by a given key. _(deprecated)_
- [- textStorageDidProcessEditing:](<nsobject-swift.class/textstoragedidprocessediting(__).md>) _(deprecated)_
- [- textStorageWillProcessEditing:](<nsobject-swift.class/textstoragewillprocessediting(__).md>) _(deprecated)_
- [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) — Sets the value of the property identified by a given key. _(deprecated)_
- [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) — Sets the value for the property identified by `key` to `value`. _(deprecated)_
- [- takeValue:forKeyPath:](<nsobject-swift.class/takevalue(__forkeypath_).md>) — Sets the value for the property identified by `keyPath` to `value`. _(deprecated)_
- [- takeValuesFromDictionary:](<nsobject-swift.class/takevalues(from_).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties _(deprecated)_
- [- unableToSetNilForKey:](<nsobject-swift.class/unabletosetnil(forkey_).md>) — Invoked if `key` is represented by a scalar attribute. _(deprecated)_
- [- valuesForKeys:](<nsobject-swift.class/values(forkeys_).md>) — Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values. _(deprecated)_
- [workflowController(_:didError:)](<../automator/amworkflowcontrollerdelegate/workflowcontroller(__diderror_).md>) — Notifies the delegate when the workflow encounters an error.
- [workflowController(_:didRun:)](<../automator/amworkflowcontrollerdelegate/workflowcontroller(__didrun_).md>) — Notifies the delegate when the specified action finishes running.
- [workflowController(_:willRun:)](<../automator/amworkflowcontrollerdelegate/workflowcontroller(__willrun_).md>) — Notifies the delegate when the specified action is about to run.
- [workflowControllerDidRun(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun(__).md>) — Notifies the delegate when the workflow controller object finishes running.
- [workflowControllerDidStop(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop(__).md>) — Tells the delegate that the workflow controller object has stopped.
- [workflowControllerWillRun(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun(__).md>) — Notifies the delegate when the workflow controller object is about to run.
- [workflowControllerWillStop(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop(__).md>) — Tells the delegate that the workflow controller object is about to stop.

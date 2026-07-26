---
title: NSObject
framework: Objective-C Runtime
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class.json'
content_hash: 'sha256:2e0ea9a8f58cef55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# NSObject

<sub>Class</sub>

The root class of most Objective-C class hierarchies, from which subclasses inherit a basic interface to the runtime system and the ability to behave as Objective-C objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSObject
```

## Relationships

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](nsobjectprotocol.md)

## Topics

### Initializing a Class

- [+ initialize](<nsobject-swift.class/initialize().md>) — Initializes the class before it receives its first message.
- [+ load](<nsobject-swift.class/load().md>) — Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.

### Creating, Copying, and Deallocating Objects

- [- init](<nsobject-swift.class/init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- copy](<nsobject-swift.class/copy().md>) — Returns the object returned by `copy(with:)`.
- [- mutableCopy](<nsobject-swift.class/mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.

### Identifying Classes

- [+ superclass](<nsobject-swift.class/superclass().md>) — Returns the class object for the receiver’s superclass.
- [+ isSubclassOfClass:](<nsobject-swift.class/issubclass(of_).md>) — Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.

### Testing Class Functionality

- [+ instancesRespondToSelector:](<nsobject-swift.class/instancesrespond(to_).md>) — Returns a Boolean value that indicates whether instances of the receiver are capable of responding to a given selector.

### Testing Protocol Conformance

- [+ conformsToProtocol:](<nsobject-swift.class/conforms(to_).md>) — Returns a Boolean value that indicates whether the target conforms to a given protocol.

### Obtaining Information About Methods

- [- methodForSelector:](<nsobject-swift.class/method(for_).md>) — Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
- [+ instanceMethodForSelector:](<nsobject-swift.class/instancemethod(for_).md>) — Locates and returns the address of the implementation of the instance method identified by a given selector.

### Describing Objects

- [+ description](<nsobject-swift.class/description().md>) — Returns a string that represents the contents of the receiving class.

### Supporting Discardable Content

- [autoContentAccessingProxy](nsobject-swift.class/autocontentaccessingproxy.md) — A proxy for the receiving object

### Sending Messages

- [- performSelector:withObject:afterDelay:](<nsobject-swift.class/perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelector:withObject:afterDelay:inModes:](<nsobject-swift.class/perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<nsobject-swift.class/performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<nsobject-swift.class/performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<nsobject-swift.class/perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<nsobject-swift.class/perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [- performSelectorInBackground:withObject:](<nsobject-swift.class/performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:](<nsobject-swift.class/cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<nsobject-swift.class/perform(__with_afterdelay_).md>) instance method.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<nsobject-swift.class/cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<nsobject-swift.class/perform(__with_afterdelay_).md>).

### Forwarding Messages

- [- forwardingTargetForSelector:](<nsobject-swift.class/forwardingtarget(for_).md>) — Returns the object to which unrecognized messages should first be directed.

### Dynamically Resolving Methods

- [+ resolveClassMethod:](<nsobject-swift.class/resolveclassmethod(__).md>) — Dynamically provides an implementation for a given selector for a class method.
- [+ resolveInstanceMethod:](<nsobject-swift.class/resolveinstancemethod(__).md>) — Dynamically provides an implementation for a given selector for an instance method.

### Handling Errors

- [- doesNotRecognizeSelector:](<nsobject-swift.class/doesnotrecognizeselector(__).md>) — Handles messages the receiver doesn’t recognize.

### Archiving

- [- awakeAfterUsingCoder:](<nsobject-swift.class/awakeafter(using_).md>) — Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [classForArchiver](nsobject-swift.class/classforarchiver.md) — The class to substitute for the receiver’s own class during archiving.
- [classForCoder](nsobject-swift.class/classforcoder.md) — Overridden by subclasses to substitute a class other than its own during coding.
- [classForKeyedArchiver](nsobject-swift.class/classforkeyedarchiver.md) — Subclasses to substitute a new class for instances during keyed archiving.
- [+ classFallbacksForKeyedArchiver](<nsobject-swift.class/classfallbacksforkeyedarchiver().md>) — Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [+ classForKeyedUnarchiver](<nsobject-swift.class/classforkeyedunarchiver().md>) — Overridden by subclasses to substitute a new class during keyed unarchiving.
- [- replacementObjectForArchiver:](<nsobject-swift.class/replacementobject(for_)-8ih2x.md>) — Overridden by subclasses to substitute another object for itself during archiving. _(deprecated)_
- [- replacementObjectForCoder:](<nsobject-swift.class/replacementobject(for_)-2l8ox.md>) — Overridden by subclasses to substitute another object for itself during encoding.
- [- replacementObjectForKeyedArchiver:](<nsobject-swift.class/replacementobject(for_)-60vwc.md>) — Overridden by subclasses to substitute another object for itself during keyed archiving.
- [+ setVersion:](<nsobject-swift.class/setversion(__).md>) — Sets the receiver’s version number.
- [+ version](<nsobject-swift.class/version().md>) — Returns the version number assigned to the class.

### Working with Class Descriptions

- [attributeKeys](nsobject-swift.class/attributekeys.md) — An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.
- [classDescription](nsobject-swift.class/classdescription.md) — An object containing information about the attributes and relationships of the receiver’s class.
- [- inverseForRelationshipKey:](<nsobject-swift.class/inverse(forrelationshipkey_).md>) — For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.
- [toManyRelationshipKeys](nsobject-swift.class/tomanyrelationshipkeys.md) — An array containing the keys for the to-many relationship properties of the receiver.
- [toOneRelationshipKeys](nsobject-swift.class/toonerelationshipkeys.md) — The keys for the to-one relationship properties of the receiver, if any.

### Improving Accessibility

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [UIAccessibilityAction](uiaccessibilityaction.md) — A set of methods that accessibility elements can use to support specific actions.
- [UIAccessibilityFocus](uiaccessibilityfocus.md) — An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityDragging](uiaccessibilitydragging.md) — A pair of properties to allow you to fine-tune how drags and drops are exposed to assistive technologies.

### Improving browser accessibility

- [- browserAccessibilityAttributedValueInRange:](<nsobject-swift.class/browseraccessibilityattributedvalue(in_).md>) — Returns the value for this element within the given range, as an attributed string.
- [- browserAccessibilityDeleteTextAtCursor:](<nsobject-swift.class/browseraccessibilitydeletetextatcursor(numberofcharacters_).md>) — Deletes text from the element at the current cursor position.
- [- browserAccessibilityInsertTextAtCursor:](<nsobject-swift.class/browseraccessibilityinserttextatcursor(text_).md>) — Inserts text into the element at the current cursor position.
- [- browserAccessibilitySelectedTextRange](<nsobject-swift.class/browseraccessibilityselectedtextrange().md>) — Returns the range of selected text in the element.
- [- browserAccessibilitySetSelectedTextRange:](<nsobject-swift.class/browseraccessibilitysetselectedtextrange(__).md>) — Updates the element’s selected text.
- [- browserAccessibilityValueInRange:](<nsobject-swift.class/browseraccessibilityvalue(in_).md>) — Returns this element’s value in the given range.
- [browserAccessibilityContainerType](nsobject-swift.class/browseraccessibilitycontainertype.md) — The kind of container that contains this element.
- [browserAccessibilityCurrentStatus](nsobject-swift.class/browseraccessibilitycurrentstatus.md) — A string that’s the element’s value for aria-current.
- [browserAccessibilityHasDOMFocus](nsobject-swift.class/browseraccessibilityhasdomfocus.md) — A Boolean value that indicates whether the element has native focus in the browser Document Object Model.
- [browserAccessibilityIsRequired](nsobject-swift.class/browseraccessibilityisrequired.md) — A Boolean value that’s the element’s value for aria-required.
- [browserAccessibilityPressedState](nsobject-swift.class/browseraccessibilitypressedstate.md) — The element’s value for aria-pressed.
- [browserAccessibilityRoleDescription](nsobject-swift.class/browseraccessibilityroledescription.md) — A string that describes the element’s role for assistive technologies.
- [browserAccessibilitySortDirection](nsobject-swift.class/browseraccessibilitysortdirection.md) — A string that’s the element’s value for aria-sort.

### Scripting

- [classCode](nsobject-swift.class/classcode.md) — The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [className](nsobject-swift.class/classname.md) — A string containing the name of the class.
- [- copyScriptingValue:forKey:withProperties:](<nsobject-swift.class/copyscriptingvalue(__forkey_withproperties_).md>) — Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<nsobject-swift.class/newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [scriptingProperties](nsobject-swift.class/scriptingproperties.md) — An `NSString`-keyed dictionary of the receiver’s scriptable properties.
- [- scriptingValueForSpecifier:](<nsobject-swift.class/scriptingvalue(for_).md>) — Given an object specifier, returns the specified object or objects in the receiving container.

### Integrating with Combine

- [KeyValueObservingPublisher](nsobject-swift.class/keyvalueobservingpublisher.md) — A Combine publisher that produces a new element whenever the observed value changes.

### Key-Value Observing

- [NSKeyValueObserving](nskeyvalueobserving.md) — An informal protocol that objects adopt to be notified of changes to the specified properties of other objects.

### Key-Value Coding

- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) — A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSKeyValueCoding](nskeyvaluecoding.md) — A mechanism by which you can access the properties of an object indirectly by name or key.
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — Exceptions raised by key-value coding methods.

### Interacting with Web Plug-ins

- [WebPlugInContainer](webplugincontainer.md) — `WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.
- [WebPlugIn](webplugin.md) — The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.

### Implementing Web Scripting

- [WebScripting](webscripting.md) — `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.

### Supporting Cocoa Scripting

- [NSScriptingComparisonMethods](nsscriptingcomparisonmethods.md) — A collection of methods useful for comparing script objects.

### Customizing accessibility

- [accessibilityElements](nsobject-swift.class/accessibilityelements.md) — An array of features of an object that assistive technologies can access.

### Deprecated

- [Deprecated Symbols](deprecated-symbols.md) — Review symbols that are no longer supported and find the replacements to use instead.

### Instance Properties

- [accessibilityActivateBlock](nsobject-swift.class/accessibilityactivateblock.md)
- [accessibilityActivationPoint](nsobject-swift.class/accessibilityactivationpoint.md)
- [accessibilityActivationPointBlock](nsobject-swift.class/accessibilityactivationpointblock.md)
- [accessibilityAttributedHint](nsobject-swift.class/accessibilityattributedhint.md)
- [accessibilityAttributedHintBlock](nsobject-swift.class/accessibilityattributedhintblock.md)
- [accessibilityAttributedLabel](nsobject-swift.class/accessibilityattributedlabel.md)
- [accessibilityAttributedLabelBlock](nsobject-swift.class/accessibilityattributedlabelblock.md)
- [accessibilityAttributedUserInputLabels](nsobject-swift.class/accessibilityattributeduserinputlabels.md)
- [accessibilityAttributedUserInputLabelsBlock](nsobject-swift.class/accessibilityattributeduserinputlabelsblock.md)
- [accessibilityAttributedValue](nsobject-swift.class/accessibilityattributedvalue.md)
- [accessibilityAttributedValueBlock](nsobject-swift.class/accessibilityattributedvalueblock.md)
- [accessibilityContainerType](nsobject-swift.class/accessibilitycontainertype.md)
- [accessibilityContainerTypeBlock](nsobject-swift.class/accessibilitycontainertypeblock.md)
- [accessibilityCustomActionsBlock](nsobject-swift.class/accessibilitycustomactionsblock.md)
- [accessibilityCustomRotors](nsobject-swift.class/accessibilitycustomrotors.md)
- [accessibilityCustomRotorsBlock](nsobject-swift.class/accessibilitycustomrotorsblock.md)
- [accessibilityDecrementBlock](nsobject-swift.class/accessibilitydecrementblock.md)
- [accessibilityDirectTouchOptions](nsobject-swift.class/accessibilitydirecttouchoptions.md)
- [accessibilityElementsBlock](nsobject-swift.class/accessibilityelementsblock.md)
- [accessibilityElementsHidden](nsobject-swift.class/accessibilityelementshidden.md)
- [accessibilityElementsHiddenBlock](nsobject-swift.class/accessibilityelementshiddenblock.md)
- [accessibilityExpandedStatus](nsobject-swift.class/accessibilityexpandedstatus.md)
- [accessibilityExpandedStatusBlock](nsobject-swift.class/accessibilityexpandedstatusblock.md)
- [accessibilityFocusedUIElement](nsobject-swift.class/accessibilityfocuseduielement.md)
- [accessibilityFrame](nsobject-swift.class/accessibilityframe.md)
- [accessibilityFrameBlock](nsobject-swift.class/accessibilityframeblock.md)
- [accessibilityHeaderElements](nsobject-swift.class/accessibilityheaderelements.md)
- [accessibilityHeaderElementsBlock](nsobject-swift.class/accessibilityheaderelementsblock.md)
- [accessibilityHint](nsobject-swift.class/accessibilityhint.md)
- [accessibilityHintBlock](nsobject-swift.class/accessibilityhintblock.md)
- [accessibilityIdentifierBlock](nsobject-swift.class/accessibilityidentifierblock.md)
- [accessibilityIncrementBlock](nsobject-swift.class/accessibilityincrementblock.md)
- [accessibilityLabel](nsobject-swift.class/accessibilitylabel.md)
- [accessibilityLabelBlock](nsobject-swift.class/accessibilitylabelblock.md)
- [accessibilityLanguage](nsobject-swift.class/accessibilitylanguage.md)
- [accessibilityLanguageBlock](nsobject-swift.class/accessibilitylanguageblock.md)
- [accessibilityMagicTapBlock](nsobject-swift.class/accessibilitymagictapblock.md)
- [accessibilityNavigationStyle](nsobject-swift.class/accessibilitynavigationstyle.md)
- [accessibilityNavigationStyleBlock](nsobject-swift.class/accessibilitynavigationstyleblock.md)
- [accessibilityNextTextNavigationElement](nsobject-swift.class/accessibilitynexttextnavigationelement.md) — An accessibility element that contains text that semantically follows this element’s text.
- [accessibilityNextTextNavigationElementBlock](nsobject-swift.class/accessibilitynexttextnavigationelementblock.md)
- [accessibilityNotifiesWhenDestroyed](nsobject-swift.class/accessibilitynotifieswhendestroyed.md) — A Boolean value that indicates whether a custom accessibility object sends a notification when its corresponding UI element is destroyed.
- [accessibilityPath](nsobject-swift.class/accessibilitypath.md)
- [accessibilityPathBlock](nsobject-swift.class/accessibilitypathblock.md)
- [accessibilityPerformEscapeBlock](nsobject-swift.class/accessibilityperformescapeblock.md)
- [accessibilityPreviousTextNavigationElement](nsobject-swift.class/accessibilityprevioustextnavigationelement.md) — An accessibility element that contains text that is semantically previous to this element’s text.
- [accessibilityPreviousTextNavigationElementBlock](nsobject-swift.class/accessibilityprevioustextnavigationelementblock.md)
- [accessibilityRespondsToUserInteraction](nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [accessibilityRespondsToUserInteractionBlock](nsobject-swift.class/accessibilityrespondstouserinteractionblock.md)
- [accessibilityShouldGroupAccessibilityChildrenBlock](nsobject-swift.class/accessibilityshouldgroupaccessibilitychildrenblock.md)
- [accessibilityTextInputResponder](nsobject-swift.class/accessibilitytextinputresponder.md) — The object that handles text input calls for this accessibility element.
- [accessibilityTextInputResponderBlock](nsobject-swift.class/accessibilitytextinputresponderblock.md) — The block to use to handle text input calls to a backing view.
- [accessibilityTextualContext](nsobject-swift.class/accessibilitytextualcontext.md)
- [accessibilityTextualContextBlock](nsobject-swift.class/accessibilitytextualcontextblock.md)
- [accessibilityTraits](nsobject-swift.class/accessibilitytraits.md)
- [accessibilityTraitsBlock](nsobject-swift.class/accessibilitytraitsblock.md)
- [accessibilityUserInputLabels](nsobject-swift.class/accessibilityuserinputlabels.md)
- [accessibilityUserInputLabelsBlock](nsobject-swift.class/accessibilityuserinputlabelsblock.md)
- [accessibilityValue](nsobject-swift.class/accessibilityvalue.md)
- [accessibilityValueBlock](nsobject-swift.class/accessibilityvalueblock.md)
- [accessibilityViewIsModal](nsobject-swift.class/accessibilityviewismodal.md)
- [accessibilityViewIsModalBlock](nsobject-swift.class/accessibilityviewismodalblock.md)
- [automationElements](nsobject-swift.class/automationelements.md)
- [automationElementsBlock](nsobject-swift.class/automationelementsblock.md)
- [browserAccessibilityDetailsElements](nsobject-swift.class/browseraccessibilitydetailselements.md)
- [browserAccessibilityImageDataSize](nsobject-swift.class/browseraccessibilityimagedatasize-swift.property.md) — Returns the native pixel dimensions of the image represented by this element, or `CGSize.zero` if this element does not represent an image. _(beta)_
- [browserAccessibilityKeyboardShortcuts](nsobject-swift.class/browseraccessibilitykeyboardshortcuts.md)
- [browserAccessibilityOrientation](nsobject-swift.class/browseraccessibilityorientation.md)
- [isAccessibilityElement](nsobject-swift.class/isaccessibilityelement.md)
- [isAccessibilityElementBlock](nsobject-swift.class/isaccessibilityelementblock.md)
- [selectable](nsobject-swift.class/isselectable.md)
- [objectSpecifier](nsobject-swift.class/objectspecifier.md) — Returns an object specifier for the receiver.
- [shouldGroupAccessibilityChildren](nsobject-swift.class/shouldgroupaccessibilitychildren.md)

### Instance Methods

- [- acceptsPreviewPanelControl:](<nsobject-swift.class/acceptspreviewpanelcontrol(__).md>)
- [- accessibilityElementAtIndex:](<nsobject-swift.class/accessibilityelement(at_).md>)
- [- accessibilityElementCount](<nsobject-swift.class/accessibilityelementcount().md>)
- [- accessibilityHitTest:](<nsobject-swift.class/accessibilityhittest(__).md>)
- [- accessibilityHitTest:withEvent:](<nsobject-swift.class/accessibilityhittest(__event_).md>)
- [- accessibilityLineEndPositionFromCurrentSelection](<nsobject-swift.class/accessibilitylineendpositionfromcurrentselection().md>)
- [- accessibilityLineRangeForPosition:](<nsobject-swift.class/accessibilitylinerange(forposition_).md>)
- [- accessibilityLineStartPositionFromCurrentSelection](<nsobject-swift.class/accessibilitylinestartpositionfromcurrentselection().md>)
- [- accessibilityZoomInAtPoint:](<nsobject-swift.class/accessibilityzoomin(at_).md>) — Zooms in on the content at the specified point.
- [- accessibilityZoomOutAtPoint:](<nsobject-swift.class/accessibilityzoomout(at_).md>) — Zooms out from the content at the specified point.
- [- actionProperty](<nsobject-swift.class/actionproperty().md>) — Sent to the delegate to request the property the action applies to.
- [- attemptRecoveryFromError:optionIndex:](<nsobject-swift.class/attemptrecovery(fromerror_optionindex_).md>) — Implemented to attempt a recovery from an error noted in an application-modal dialog.
- [- attemptRecoveryFromError:optionIndex:delegate:didRecoverSelector:contextInfo:](<nsobject-swift.class/attemptrecovery(fromerror_optionindex_delegate_didrecoverselector_contextinfo_).md>) — Implemented to attempt a recovery from an error noted in a document-modal sheet.
- [- authorizationViewCreatedAuthorization:](<nsobject-swift.class/authorizationviewcreatedauthorization(__).md>) — Sent to the delegate to indicate the authorization object has been created or changed.
- [- authorizationViewDidAuthorize:](<nsobject-swift.class/authorizationviewdidauthorize(__).md>) — Sent to the delegate to indicate the user was authorized and the authorization view was changed to unlocked.
- [- authorizationViewDidDeauthorize:](<nsobject-swift.class/authorizationviewdiddeauthorize(__).md>) — Sent to the delegate to indicate the user was deauthorized and the authorization view was changed to locked.
- [- authorizationViewDidHide:](<nsobject-swift.class/authorizationviewdidhide(__).md>) — Sent to the delegate to indicate that the view’s visibility has changed.
- [- authorizationViewReleasedAuthorization:](<nsobject-swift.class/authorizationviewreleasedauthorization(__).md>) — Sent to the delegate to indicate that deauthorization is about to occur.
- [- authorizationViewShouldDeauthorize:](<nsobject-swift.class/authorizationviewshoulddeauthorize(__).md>) — Sent to the delegate when a user clicks the open lock icon.
- [- awakeFromNib](<nsobject-swift.class/awakefromnib().md>) — Prepares the receiver for service after it has been loaded from an Interface Builder archive, or nib file.
- [- beginPreviewPanelControl:](<nsobject-swift.class/beginpreviewpanelcontrol(__).md>)
- [- browserAccessibilityImageData:](<nsobject-swift.class/browseraccessibilityimagedata(__).md>)
- [- burnProgressPanel:burnDidFinish:](<nsobject-swift.class/burnprogresspanel(__burndidfinish_).md>) — Allows the delegate to handle the end-of-burn feedback.
- [- burnProgressPanelDidFinish:](<nsobject-swift.class/burnprogresspaneldidfinish(__).md>) — Notification sent by the panel after ordering out.
- [- burnProgressPanelWillBegin:](<nsobject-swift.class/burnprogresspanelwillbegin(__).md>) — Notification sent by the panel before display.
- [- candidates:](<nsobject-swift.class/candidates(__).md>) — Returns an array of candidates.
- [- certificatePanelShowHelp:](<nsobject-swift.class/certificatepanelshowhelp(__).md>) — Implements custom help behavior for the modal panel.
- [- chooseIdentityPanelShowHelp:](<nsobject-swift.class/chooseidentitypanelshowhelp(__).md>) — Implements custom help behavior for the modal panel.
- [- commitComposition:](<nsobject-swift.class/commitcomposition(__).md>) — Informs the controller that the composition should be committed.
- [- composedString:](<nsobject-swift.class/composedstring(__).md>) — Return the current composed string.
- [- compositionParameterView:didChangeParameterWithKey:](<nsobject-swift.class/compositionparameterview(__didchangeparameterwithkey_).md>) — Called after an input parameter in the composition parameter view has been edited. _(deprecated)_
- [- compositionParameterView:shouldDisplayParameterWithKey:attributes:](<nsobject-swift.class/compositionparameterview(__shoulddisplayparameterwithkey_attributes_).md>) — Allows you to define which composition parameters are visible in the user interface when the composition parameter view refreshes. _(deprecated)_
- [- compositionPickerView:didSelectComposition:](<nsobject-swift.class/compositionpickerview(__didselect_).md>) — Performs custom tasks when the selected composition in the composition picker view changes. _(deprecated)_
- [- compositionPickerViewDidStartAnimating:](<nsobject-swift.class/compositionpickerviewdidstartanimating(__).md>) — Performs custom tasks when the composition picker view starts animating a composition. _(deprecated)_
- [- compositionPickerViewWillStopAnimating:](<nsobject-swift.class/compositionpickerviewwillstopanimating(__).md>) — Performs custom tasks when the composition picker view stops animating a composition. _(deprecated)_
- [- didCommandBySelector:client:](<nsobject-swift.class/didcommand(by_client_).md>) — Processes a command  generated by user action such as typing certain keys or pressing the mouse button.
- [- doesContain:](<nsobject-swift.class/doescontain(__).md>) — Returns a Boolean value that indicates whether the receiver contains a given object.
- [- endPreviewPanelControl:](<nsobject-swift.class/endpreviewpanelcontrol(__).md>)
- [- eraseProgressPanel:eraseDidFinish:](<nsobject-swift.class/eraseprogresspanel(__erasedidfinish_).md>) — Notification sent by the panel before display.
- [- eraseProgressPanelDidFinish:](<nsobject-swift.class/eraseprogresspaneldidfinish(__).md>) — Notification sent by the panel after ordering out.
- [- eraseProgressPanelWillBegin:](<nsobject-swift.class/eraseprogresspanelwillbegin(__).md>) — Notification sent by the panel before display.
- [- exceptionHandler:shouldHandleException:mask:](<nsobject-swift.class/exceptionhandler(__shouldhandle_mask_).md>) — Implemented by the delegate to evaluate whether the delegating exception handler should handle a given exception.
- [- exceptionHandler:shouldLogException:mask:](<nsobject-swift.class/exceptionhandler(__shouldlogexception_mask_).md>) — Implemented by the delegate to evaluate whether the delegating exception hangler should log a given exception.
- [- fileTransferServicesAbortComplete:error:](<nsobject-swift.class/filetransferservicesabortcomplete(__error_).md>)
- [- fileTransferServicesConnectionComplete:error:](<nsobject-swift.class/filetransferservicesconnectioncomplete(__error_).md>)
- [- fileTransferServicesCopyRemoteFileComplete:error:](<nsobject-swift.class/filetransferservicescopyremotefilecomplete(__error_).md>)
- [- fileTransferServicesCopyRemoteFileProgress:transferProgress:](<nsobject-swift.class/filetransferservicescopyremotefileprogress(__transferprogress_).md>)
- [- fileTransferServicesCreateFolderComplete:error:folder:](<nsobject-swift.class/filetransferservicescreatefoldercomplete(__error_folder_).md>)
- [- fileTransferServicesDisconnectionComplete:error:](<nsobject-swift.class/filetransferservicesdisconnectioncomplete(__error_).md>)
- [- fileTransferServicesFilePreparationComplete:error:](<nsobject-swift.class/filetransferservicesfilepreparationcomplete(__error_).md>)
- [- fileTransferServicesPathChangeComplete:error:finalPath:](<nsobject-swift.class/filetransferservicespathchangecomplete(__error_finalpath_).md>)
- [- fileTransferServicesRemoveItemComplete:error:removedItem:](<nsobject-swift.class/filetransferservicesremoveitemcomplete(__error_removeditem_).md>)
- [- fileTransferServicesRetrieveFolderListingComplete:error:listing:](<nsobject-swift.class/filetransferservicesretrievefolderlistingcomplete(__error_listing_).md>)
- [- fileTransferServicesSendFileComplete:error:](<nsobject-swift.class/filetransferservicessendfilecomplete(__error_).md>)
- [- fileTransferServicesSendFileProgress:transferProgress:](<nsobject-swift.class/filetransferservicessendfileprogress(__transferprogress_).md>)
- [- handleEvent:client:](<nsobject-swift.class/handle(__client_).md>) — Handles key down and mouse events.
- [- imageBrowser:backgroundWasRightClickedWithEvent:](<nsobject-swift.class/imagebrowser(__backgroundwasrightclickedwith_).md>) — Performs custom tasks when the user right-clicks the image browser view background.
- [- imageBrowser:cellWasDoubleClickedAtIndex:](<nsobject-swift.class/imagebrowser(__cellwasdoubleclickedat_).md>) — Performs custom tasks when the user double-clicks an item in the image browser view.
- [- imageBrowser:cellWasRightClickedAtIndex:withEvent:](<nsobject-swift.class/imagebrowser(__cellwasrightclickedat_with_).md>) — Performs custom tasks when the user right-clicks an item in the image browser view.
- [- imageBrowser:groupAtIndex:](<nsobject-swift.class/imagebrowser(__groupat_).md>) — Returns the group at the specified index.
- [- imageBrowser:itemAtIndex:](<nsobject-swift.class/imagebrowser(__itemat_).md>) — Returns an object for the item in an image browser view that corresponds to the specified index.
- [- imageBrowser:moveItemsAtIndexes:toIndex:](<nsobject-swift.class/imagebrowser(__moveitemsat_to_).md>) — Signals that the specified items should be moved to the specified destination.
- [- imageBrowser:removeItemsAtIndexes:](<nsobject-swift.class/imagebrowser(__removeitemsat_).md>) — Signals that a remove operation should be applied to the specified items.
- [- imageBrowser:writeItemsAtIndexes:toPasteboard:](<nsobject-swift.class/imagebrowser(__writeitemsat_to_).md>) — Signals that a drag should begin.
- [- imageBrowserSelectionDidChange:](<nsobject-swift.class/imagebrowserselectiondidchange(__).md>) — Performs custom tasks when the selection changes.
- [- imageRepresentation](<nsobject-swift.class/imagerepresentation().md>) — Returns the image to display.
- [- imageRepresentationType](<nsobject-swift.class/imagerepresentationtype().md>) — Returns the representation type of the image to display.
- [- imageSubtitle](<nsobject-swift.class/imagesubtitle().md>) — Returns the display subtitle of the image.
- [- imageTitle](<nsobject-swift.class/imagetitle().md>) — Returns the display title of the image.
- [- imageUID](<nsobject-swift.class/imageuid().md>) — Returns a unique string that identifies the data source item.
- [- imageVersion](<nsobject-swift.class/imageversion().md>) — Returns the version of the item.
- [- indexOfAccessibilityElement:](<nsobject-swift.class/index(ofaccessibilityelement_).md>)
- [- indicesOfObjectsByEvaluatingObjectSpecifier:](<nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier_).md>) — Returns the indices of the specified container objects.
- [- inputText:client:](<nsobject-swift.class/inputtext(__client_).md>) — Handles key down events that do not map to an action method.
- [- inputText:key:modifiers:client:](<nsobject-swift.class/inputtext(__key_modifiers_client_).md>) — Receives Unicode, the key code that generated it, and any modifier flags.
- [- isCaseInsensitiveLike:](<nsobject-swift.class/iscaseinsensitivelike(__).md>) — Returns a Boolean value that indicates whether receiver is considered to be “like” a given string when the case of characters in the receiver is ignored.
- [- isEqualTo:](<nsobject-swift.class/isequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is equal to another given object.
- [- isGreaterThan:](<nsobject-swift.class/isgreaterthan(__).md>) — Returns a Boolean value that indicates whether the receiver is greater than another given object.
- [- isGreaterThanOrEqualTo:](<nsobject-swift.class/isgreaterthanorequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is greater than or equal to another given object.
- [- isLessThan:](<nsobject-swift.class/islessthan(__).md>) — Returns a Boolean value that indicates whether the receiver is less than another given object.
- [- isLessThanOrEqualTo:](<nsobject-swift.class/islessthanorequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is less than or equal to another given object.
- [- isLike:](<nsobject-swift.class/islike(__).md>) — Returns a Boolean value that indicates whether the receiver is “like” another given object.
- [- isNotEqualTo:](<nsobject-swift.class/isnotequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is not equal to another given object.
- [- numberOfGroupsInImageBrowser:](<nsobject-swift.class/numberofgroups(inimagebrowser_).md>) — Returns the number of groups in an image browser view.
- [- numberOfItemsInImageBrowser:](<nsobject-swift.class/numberofitems(inimagebrowser_).md>) — Returns the number of records managed by the data source object.
- [- originalString:](<nsobject-swift.class/originalstring(__).md>) — Return the string that consists of the precomposed Unicode characters.
- [- performActionForPerson:identifier:](<nsobject-swift.class/performaction(for_identifier_).md>) — Sent to the delegate to perform the action.
- [- prepareForInterfaceBuilder](<nsobject-swift.class/prepareforinterfacebuilder().md>) — Called when a designable object is created in Interface Builder.
- [- provideImageToMTLTexture:commandBuffer:originx:originy:width:height:userInfo:](<nsobject-swift.class/provideimage(to_commandbuffer_originx_originy_width_height_userinfo_).md>) — An optional method that an image provider object may implement.
With this method, the provider object can use the Metal API to provide pixel
data into a MTLTexture when the image object is rendered.
- [- provideImageData:bytesPerRow:origin::size::userInfo:](<nsobject-swift.class/provideimagedata(__bytesperrow_origin___size___userinfo_).md>) — Supplies data to a `CIImage` object.
- [- quartzFilterManager:didAddFilter:](<nsobject-swift.class/quartzfiltermanager(__didadd_).md>)
- [- quartzFilterManager:didModifyFilter:](<nsobject-swift.class/quartzfiltermanager(__didmodifyfilter_).md>)
- [- quartzFilterManager:didRemoveFilter:](<nsobject-swift.class/quartzfiltermanager(__didremove_).md>)
- [- quartzFilterManager:didSelectFilter:](<nsobject-swift.class/quartzfiltermanager(__didselect_).md>)
- [- readLinkQualityForDeviceComplete:device:info:error:](<nsobject-swift.class/readlinkquality(fordevicecomplete_device_info_error_).md>)
- [- readRSSIForDeviceComplete:device:info:error:](<nsobject-swift.class/readrssi(fordevicecomplete_device_info_error_).md>)
- [- saveOptions:shouldShowUTType:](<nsobject-swift.class/saveoptions(__shouldshowuttype_).md>) — Called to determine if the specified uniform type identifier should be shown in the save panel.
- [- setSharedObservers:](<nsobject-swift.class/setsharedobservers(__).md>)
- [- setupPanel:determineBestDeviceOfA:orB:](<nsobject-swift.class/setuppanel(__determinebestdeviceofa_orb_).md>) — Allows the delegate to specify which device is its preferred.
- [- setupPanel:deviceContainsSuitableMedia:promptString:](<nsobject-swift.class/setuppanel(__devicecontainssuitablemedia_promptstring_).md>) — This delegate method allows the delegate to determine if the media inserted in the device is suitable for whatever operation is to be performed.
- [- setupPanel:deviceCouldBeTarget:](<nsobject-swift.class/setuppanel(__devicecouldbetarget_).md>) — Allows the delegate to determine if device can be used as a target.
- [- setupPanelDeviceSelectionChanged:](<nsobject-swift.class/setuppaneldeviceselectionchanged(__).md>) — Sent by the default notification center when the device selection in the panel has changed.
- [- setupPanelShouldHandleMediaReservations:](<nsobject-swift.class/setuppanelshouldhandlemediareservations(__).md>) — This delegate method allows the delegate to control how media reservations are handled.
- [- shouldEnableActionForPerson:identifier:](<nsobject-swift.class/shouldenableaction(for_identifier_).md>) — Sent to the delegate to determine whether the action should be enabled.
- [- titleForPerson:identifier:](<nsobject-swift.class/title(for_identifier_).md>) — Sent to the delegate to request the title of the menu item for the action.
- [- workflowController:didError:](<nsobject-swift.class/workflowcontroller(__diderror_).md>) _(deprecated)_
- [- workflowController:didRunAction:](<nsobject-swift.class/workflowcontroller(__didrun_).md>) _(deprecated)_
- [- workflowController:willRunAction:](<nsobject-swift.class/workflowcontroller(__willrun_).md>) _(deprecated)_
- [- workflowControllerDidRun:](<nsobject-swift.class/workflowcontrollerdidrun(__).md>) _(deprecated)_
- [- workflowControllerDidStop:](<nsobject-swift.class/workflowcontrollerdidstop(__).md>) _(deprecated)_
- [- workflowControllerWillRun:](<nsobject-swift.class/workflowcontrollerwillrun(__).md>) _(deprecated)_
- [- workflowControllerWillStop:](<nsobject-swift.class/workflowcontrollerwillstop(__).md>) _(deprecated)_

### Type Methods

- [+ debugDescription](<nsobject-swift.class/debugdescription().md>)
- [+ hash](<nsobject-swift.class/hash().md>)

### Default Implementations

- [Equatable Implementations](nsobject-swift.class/equatable-implementations.md)
- [Hashable Implementations](nsobject-swift.class/hashable-implementations.md)

## See Also

### Classes

- [Protocol](protocol.md)

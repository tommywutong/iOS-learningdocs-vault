---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Automator.html
archived_at: '2026-07-18T02:53:21.404053Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Automator Changes for Swift

### Automator

Removed [AMBundleAction.init(definition: [NSObject : AnyObject]!, fromArchive: Bool)](https://developer.apple.com/documentation/automator/ambundleaction/1807582-initwithdefinition)Removed AMShellScriptAction.inputFieldSeparator() -> String!Removed AMShellScriptAction.outputFieldSeparator() -> String!Removed AMShellScriptAction.remapLineEndings() -> BoolAdded [AMShellScriptAction.inputFieldSeparator](https://developer.apple.com/documentation/automator/amshellscriptaction/1419760-inputfieldseparator)Added [AMShellScriptAction.outputFieldSeparator](https://developer.apple.com/documentation/automator/amshellscriptaction/1419636-outputfieldseparator)Added [AMShellScriptAction.remapLineEndings](https://developer.apple.com/documentation/automator/amshellscriptaction/1419681-remaplineendings)Added [AMWorkflow.init()](https://developer.apple.com/documentation/automator/amworkflow/1419602-init)Modified [AMAction](https://developer.apple.com/documentation/automator/amaction)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class AMAction : NSObject {     init!(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool)     init!(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer)     var name: String! { get }     var ignoresInput: Bool { get }     var selectedInputType: String!     var selectedOutputType: String!     var progressValue: CGFloat     func runWithInput(_ input: AnyObject!, fromAction anAction: AMAction!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> AnyObject!     func runWithInput(_ input: AnyObject!, error error: NSErrorPointer) -> AnyObject!     func runAsynchronouslyWithInput(_ input: AnyObject!)     func willFinishRunning()     func didFinishRunningWithError(_ errorInfo: [NSObject : AnyObject]!)     func finishRunningWithError(_ error: NSError!)     var output: AnyObject!     func stop()     func reset()     func writeToDictionary(_ dictionary: NSMutableDictionary!)     func opened()     func activated()     func closed()     func updateParameters()     func parametersUpdated()     var stopped: Bool { get } } ``` | OS X 10.10 |
| To | ``` class AMAction : NSObject {     init?(definition dict: [String : AnyObject], fromArchive archived: Bool)     init(contentsOfURL fileURL: NSURL) throws     var name: String { get }     var ignoresInput: Bool { get }     var selectedInputType: String?     var selectedOutputType: String?     var progressValue: CGFloat     func runWithInput(_ input: AnyObject?, fromAction anAction: AMAction?, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> AnyObject?     func runWithInput(_ input: AnyObject?) throws -> AnyObject     func runAsynchronouslyWithInput(_ input: AnyObject?)     func willFinishRunning()     func didFinishRunningWithError(_ errorInfo: [String : AnyObject]?)     func finishRunningWithError(_ error: NSError?)     var output: AnyObject?     func stop()     func reset()     func writeToDictionary(_ dictionary: NSMutableDictionary)     func opened()     func activated()     func closed()     func updateParameters()     func parametersUpdated()     var stopped: Bool { get } } ``` | OS X 10.4 |

Modified [AMAction.finishRunningWithError(_: NSError?)](https://developer.apple.com/documentation/automator/amaction/1419677-finishrunningwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func finishRunningWithError(_ error: NSError!) ``` |
| To | ``` func finishRunningWithError(_ error: NSError?) ``` |

Modified [AMAction.init(contentsOfURL: NSURL) throws](https://developer.apple.com/documentation/automator/amaction/1419742-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init(contentsOfURL fileURL: NSURL) throws ``` |

Modified [AMAction.init(definition: [String : AnyObject], fromArchive: Bool)](https://developer.apple.com/documentation/automator/amaction/1419574-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool) ``` |
| To | ``` init?(definition dict: [String : AnyObject], fromArchive archived: Bool) ``` |

Modified [AMAction.name](https://developer.apple.com/documentation/automator/amaction/1419648-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [AMAction.output](https://developer.apple.com/documentation/automator/amaction/1419786-output)

|  | Declaration |
| --- | --- |
| From | ``` var output: AnyObject! ``` |
| To | ``` var output: AnyObject? ``` |

Modified [AMAction.runAsynchronouslyWithInput(_: AnyObject?)](https://developer.apple.com/documentation/automator/amaction/1419691-runasynchronously)

|  | Declaration |
| --- | --- |
| From | ``` func runAsynchronouslyWithInput(_ input: AnyObject!) ``` |
| To | ``` func runAsynchronouslyWithInput(_ input: AnyObject?) ``` |

Modified [AMAction.runWithInput(_: AnyObject?) throws -> AnyObject](https://developer.apple.com/documentation/automator/amaction/1419624-run)

|  | Declaration |
| --- | --- |
| From | ``` func runWithInput(_ input: AnyObject!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func runWithInput(_ input: AnyObject?) throws -> AnyObject ``` |

Modified [AMAction.selectedInputType](https://developer.apple.com/documentation/automator/amaction/1419756-selectedinputtype)

|  | Declaration |
| --- | --- |
| From | ``` var selectedInputType: String! ``` |
| To | ``` var selectedInputType: String? ``` |

Modified [AMAction.selectedOutputType](https://developer.apple.com/documentation/automator/amaction/1419661-selectedoutputtype)

|  | Declaration |
| --- | --- |
| From | ``` var selectedOutputType: String! ``` |
| To | ``` var selectedOutputType: String? ``` |

Modified [AMAction.writeToDictionary(_: NSMutableDictionary)](https://developer.apple.com/documentation/automator/amaction/1419736-writetodictionary)

|  | Declaration |
| --- | --- |
| From | ``` func writeToDictionary(_ dictionary: NSMutableDictionary!) ``` |
| To | ``` func writeToDictionary(_ dictionary: NSMutableDictionary) ``` |

Modified [AMAppleScriptAction](https://developer.apple.com/documentation/automator/amapplescriptaction)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class AMAppleScriptAction : AMBundleAction {     var script: OSAScript! } ``` | OS X 10.10 |
| To | ``` class AMAppleScriptAction : AMBundleAction {     var script: OSAScript } ``` | OS X 10.4 |

Modified [AMAppleScriptAction.script](https://developer.apple.com/documentation/automator/amapplescriptaction/1419700-script)

|  | Declaration |
| --- | --- |
| From | ``` var script: OSAScript! ``` |
| To | ``` var script: OSAScript ``` |

Modified [AMBundleAction](https://developer.apple.com/documentation/automator/ambundleaction)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class AMBundleAction : AMAction, NSCoding, NSCopying {     init!(definition dict: [NSObject : AnyObject]!, fromArchive archived: Bool)     func awakeFromBundle()     var hasView: Bool { get }     var view: NSView! { get }     var bundle: NSBundle! { get }     var parameters: NSMutableDictionary! } ``` | OS X 10.10 |
| To | ``` class AMBundleAction : AMAction, NSCoding, NSCopying {     func awakeFromBundle()     var hasView: Bool { get }     var view: NSView? { get }     var bundle: NSBundle { get }     var parameters: NSMutableDictionary? } ``` | OS X 10.4 |

Modified [AMBundleAction.bundle](https://developer.apple.com/documentation/automator/ambundleaction/1419572-bundle)

|  | Declaration |
| --- | --- |
| From | ``` var bundle: NSBundle! { get } ``` |
| To | ``` var bundle: NSBundle { get } ``` |

Modified [AMBundleAction.parameters](https://developer.apple.com/documentation/automator/ambundleaction/1419634-parameters)

|  | Declaration |
| --- | --- |
| From | ``` var parameters: NSMutableDictionary! ``` |
| To | ``` var parameters: NSMutableDictionary? ``` |

Modified [AMBundleAction.view](https://developer.apple.com/documentation/automator/ambundleaction/1419665-view)

|  | Declaration |
| --- | --- |
| From | ``` var view: NSView! { get } ``` |
| To | ``` var view: NSView? { get } ``` |

Modified [AMLogLevel [enum]](https://developer.apple.com/documentation/automator/amloglevel)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [AMShellScriptAction](https://developer.apple.com/documentation/automator/amshellscriptaction)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class AMShellScriptAction : AMBundleAction {     func remapLineEndings() -> Bool     func inputFieldSeparator() -> String!     func outputFieldSeparator() -> String! } ``` | OS X 10.10 |
| To | ``` class AMShellScriptAction : AMBundleAction {     var remapLineEndings: Bool { get }     var inputFieldSeparator: String { get }     var outputFieldSeparator: String { get } } ``` | OS X 10.4 |

Modified [AMWorkflow](https://developer.apple.com/documentation/automator/amworkflow)

|  | Declaration |
| --- | --- |
| From | ``` class AMWorkflow : NSObject, NSCopying {     class func runWorkflowAtURL(_ fileURL: NSURL!, withInput input: AnyObject!, error error: NSErrorPointer) -> AnyObject!     init!(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer)     func writeToURL(_ fileURL: NSURL!, error outError: NSErrorPointer) -> Bool     func setValue(_ value: AnyObject!, forVariableWithName variableName: String!) -> Bool     func valueForVariableWithName(_ variableName: String!) -> AnyObject!     func addAction(_ action: AMAction!)     func removeAction(_ action: AMAction!)     func insertAction(_ action: AMAction!, atIndex index: Int)     func moveActionAtIndex(_ startIndex: Int, toIndex endIndex: Int)     @NSCopying var fileURL: NSURL! { get }     var actions: [AnyObject]! { get }     var input: AnyObject!     var output: AnyObject! { get } } ``` |
| To | ``` class AMWorkflow : NSObject, NSCopying {     class func runWorkflowAtURL(_ fileURL: NSURL, withInput input: AnyObject?) throws -> AnyObject     init()     convenience init(contentsOfURL fileURL: NSURL) throws     func writeToURL(_ fileURL: NSURL) throws     func setValue(_ value: AnyObject?, forVariableWithName variableName: String) -> Bool     func valueForVariableWithName(_ variableName: String) -> AnyObject     func addAction(_ action: AMAction)     func removeAction(_ action: AMAction)     func insertAction(_ action: AMAction, atIndex index: Int)     func moveActionAtIndex(_ startIndex: Int, toIndex endIndex: Int)     @NSCopying var fileURL: NSURL? { get }     var actions: [AMAction] { get }     var input: AnyObject?     var output: AnyObject? { get } } ``` |

Modified [AMWorkflow.actions](https://developer.apple.com/documentation/automator/amworkflow/1419646-actions)

|  | Declaration |
| --- | --- |
| From | ``` var actions: [AnyObject]! { get } ``` |
| To | ``` var actions: [AMAction] { get } ``` |

Modified [AMWorkflow.addAction(_: AMAction)](https://developer.apple.com/documentation/automator/amworkflow/1419708-addaction)

|  | Declaration |
| --- | --- |
| From | ``` func addAction(_ action: AMAction!) ``` |
| To | ``` func addAction(_ action: AMAction) ``` |

Modified [AMWorkflow.fileURL](https://developer.apple.com/documentation/automator/amworkflow/1419726-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fileURL: NSURL! { get } ``` |
| To | ``` @NSCopying var fileURL: NSURL? { get } ``` |

Modified [AMWorkflow.init(contentsOfURL: NSURL) throws](https://developer.apple.com/documentation/automator/amworkflow/1419774-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL fileURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` convenience init(contentsOfURL fileURL: NSURL) throws ``` |

Modified [AMWorkflow.input](https://developer.apple.com/documentation/automator/amworkflow/1419587-input)

|  | Declaration |
| --- | --- |
| From | ``` var input: AnyObject! ``` |
| To | ``` var input: AnyObject? ``` |

Modified [AMWorkflow.insertAction(_: AMAction, atIndex: Int)](https://developer.apple.com/documentation/automator/amworkflow/1419714-insertaction)

|  | Declaration |
| --- | --- |
| From | ``` func insertAction(_ action: AMAction!, atIndex index: Int) ``` |
| To | ``` func insertAction(_ action: AMAction, atIndex index: Int) ``` |

Modified [AMWorkflow.output](https://developer.apple.com/documentation/automator/amworkflow/1419626-output)

|  | Declaration |
| --- | --- |
| From | ``` var output: AnyObject! { get } ``` |
| To | ``` var output: AnyObject? { get } ``` |

Modified [AMWorkflow.removeAction(_: AMAction)](https://developer.apple.com/documentation/automator/amworkflow/1419604-removeaction)

|  | Declaration |
| --- | --- |
| From | ``` func removeAction(_ action: AMAction!) ``` |
| To | ``` func removeAction(_ action: AMAction) ``` |

Modified [AMWorkflow.runWorkflowAtURL(_: NSURL, withInput: AnyObject?) throws -> AnyObject [class]](https://developer.apple.com/documentation/automator/amworkflow/1419750-run)

|  | Declaration |
| --- | --- |
| From | ``` class func runWorkflowAtURL(_ fileURL: NSURL!, withInput input: AnyObject!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` class func runWorkflowAtURL(_ fileURL: NSURL, withInput input: AnyObject?) throws -> AnyObject ``` |

Modified [AMWorkflow.setValue(_: AnyObject?, forVariableWithName: String) -> Bool](https://developer.apple.com/documentation/automator/amworkflow/1419768-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forVariableWithName variableName: String!) -> Bool ``` |
| To | ``` func setValue(_ value: AnyObject?, forVariableWithName variableName: String) -> Bool ``` |

Modified [AMWorkflow.valueForVariableWithName(_: String) -> AnyObject](https://developer.apple.com/documentation/automator/amworkflow/1419622-valueforvariablewithname)

|  | Declaration |
| --- | --- |
| From | ``` func valueForVariableWithName(_ variableName: String!) -> AnyObject! ``` |
| To | ``` func valueForVariableWithName(_ variableName: String) -> AnyObject ``` |

Modified [AMWorkflow.writeToURL(_: NSURL) throws](https://developer.apple.com/documentation/automator/amworkflow/1419685-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ fileURL: NSURL!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func writeToURL(_ fileURL: NSURL) throws ``` |

Modified [AMWorkflowController](https://developer.apple.com/documentation/automator/amworkflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class AMWorkflowController : NSController {     var workflow: AMWorkflow!     var workflowView: AMWorkflowView!     unowned(unsafe) var delegate: AnyObject!     var canRun: Bool { get }     var running: Bool { get }     @IBAction func run(_ sender: AnyObject!)     @IBAction func stop(_ sender: AnyObject!)     var paused: Bool { get }     @IBAction func pause(_ sender: AnyObject!)     @IBAction func step(_ sender: AnyObject!)     @IBAction func reset(_ sender: AnyObject!) } ``` |
| To | ``` class AMWorkflowController : NSController {     var workflow: AMWorkflow?     var workflowView: AMWorkflowView?     unowned(unsafe) var delegate: AnyObject?     var canRun: Bool { get }     var running: Bool { get }     @IBAction func run(_ sender: AnyObject)     @IBAction func stop(_ sender: AnyObject)     var paused: Bool { get }     @IBAction func pause(_ sender: AnyObject)     @IBAction func step(_ sender: AnyObject)     @IBAction func reset(_ sender: AnyObject) } ``` |

Modified [AMWorkflowController.delegate](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419724-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject? ``` |

Modified [AMWorkflowController.pause(_: AnyObject)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419659-pause)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func pause(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func pause(_ sender: AnyObject) ``` |

Modified [AMWorkflowController.reset(_: AnyObject)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419748-reset)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func reset(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func reset(_ sender: AnyObject) ``` |

Modified [AMWorkflowController.run(_: AnyObject)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419780-run)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func run(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func run(_ sender: AnyObject) ``` |

Modified [AMWorkflowController.step(_: AnyObject)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419740-step)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func step(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func step(_ sender: AnyObject) ``` |

Modified [AMWorkflowController.stop(_: AnyObject)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419712-stop)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stop(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func stop(_ sender: AnyObject) ``` |

Modified [AMWorkflowController.workflow](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419620-workflow)

|  | Declaration |
| --- | --- |
| From | ``` var workflow: AMWorkflow! ``` |
| To | ``` var workflow: AMWorkflow? ``` |

Modified [AMWorkflowController.workflowView](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419614-workflowview)

|  | Declaration |
| --- | --- |
| From | ``` var workflowView: AMWorkflowView! ``` |
| To | ``` var workflowView: AMWorkflowView? ``` |

Modified [AMWorkflowView](https://developer.apple.com/documentation/automator/amworkflowview)

|  | Declaration |
| --- | --- |
| From | ``` class AMWorkflowView : NSView {     var editable: Bool     var workflowController: AMWorkflowController! } ``` |
| To | ``` class AMWorkflowView : NSView {     var editable: Bool     var workflowController: AMWorkflowController? } ``` |

Modified [AMWorkflowView.workflowController](https://developer.apple.com/documentation/automator/amworkflowview/1419790-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` var workflowController: AMWorkflowController! ``` |
| To | ``` var workflowController: AMWorkflowController? ``` |

Modified [NSObject.workflowController(_: AMWorkflowController, didError: NSError)](https://developer.apple.com/documentation/objectivec/nsobject/1419652-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func workflowController(_ controller: AMWorkflowController!, didError error: NSError!) ``` |
| To | ``` func workflowController(_ controller: AMWorkflowController, didError error: NSError) ``` |

Modified [NSObject.workflowController(_: AMWorkflowController, didRunAction: AMAction)](https://developer.apple.com/documentation/objectivec/nsobject/1419675-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func workflowController(_ controller: AMWorkflowController!, didRunAction action: AMAction!) ``` |
| To | ``` func workflowController(_ controller: AMWorkflowController, didRunAction action: AMAction) ``` |

Modified [NSObject.workflowController(_: AMWorkflowController, willRunAction: AMAction)](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419720-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func workflowController(_ controller: AMWorkflowController!, willRunAction action: AMAction!) ``` |
| To | ``` func workflowController(_ controller: AMWorkflowController, willRunAction action: AMAction) ``` |

Modified [NSObject.workflowControllerDidRun(_: AMWorkflowController)](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419762-workflowcontrollerdidrun)

|  | Declaration |
| --- | --- |
| From | ``` func workflowControllerDidRun(_ controller: AMWorkflowController!) ``` |
| To | ``` func workflowControllerDidRun(_ controller: AMWorkflowController) ``` |

Modified [NSObject.workflowControllerDidStop(_: AMWorkflowController)](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419770-workflowcontrollerdidstop)

|  | Declaration |
| --- | --- |
| From | ``` func workflowControllerDidStop(_ controller: AMWorkflowController!) ``` |
| To | ``` func workflowControllerDidStop(_ controller: AMWorkflowController) ``` |

Modified [NSObject.workflowControllerWillRun(_: AMWorkflowController)](https://developer.apple.com/documentation/objectivec/nsobject/1419730-workflowcontrollerwillrun)

|  | Declaration |
| --- | --- |
| From | ``` func workflowControllerWillRun(_ controller: AMWorkflowController!) ``` |
| To | ``` func workflowControllerWillRun(_ controller: AMWorkflowController) ``` |

Modified [NSObject.workflowControllerWillStop(_: AMWorkflowController)](https://developer.apple.com/documentation/objectivec/nsobject/1419598-workflowcontrollerwillstop)

|  | Declaration |
| --- | --- |
| From | ``` func workflowControllerWillStop(_ controller: AMWorkflowController!) ``` |
| To | ``` func workflowControllerWillStop(_ controller: AMWorkflowController) ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

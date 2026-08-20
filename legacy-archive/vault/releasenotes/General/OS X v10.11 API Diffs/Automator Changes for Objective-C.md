---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/Automator.html
archived_at: '2026-07-18T02:52:56.239580Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Automator Changes for Objective-C

### Automator

#### AMAction.h

Modified -[AMAction definition]

|  | Declaration |
| --- | --- |
| From | ``` - (NSMutableDictionary *)definition ``` |
| To | ``` - (NSMutableDictionary<NSString *,id> * _Nonnull)definition ``` |

Modified [-[AMAction didFinishRunningWithError:]](https://developer.apple.com/documentation/automator/amaction/1438357-didfinishrunningwitherror)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didFinishRunningWithError:(NSDictionary *)errorInfo ``` |
| To | ``` - (void)didFinishRunningWithError:(NSDictionary<NSString *,id> * _Nullable)errorInfo ``` |

Modified [-[AMAction finishRunningWithError:]](https://developer.apple.com/documentation/automator/amaction/1419677-finishrunningwitherror)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishRunningWithError:(NSError *)error ``` |
| To | ``` - (void)finishRunningWithError:(NSError * _Nullable)error ``` |

Modified [-[AMAction initWithContentsOfURL:error:]](https://developer.apple.com/documentation/automator/amaction/1419742-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)fileURL error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)fileURL error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AMAction initWithDefinition:fromArchive:]](https://developer.apple.com/documentation/automator/amaction/1419574-initwithdefinition)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDefinition:(NSDictionary *)dict fromArchive:(BOOL)archived ``` |
| To | ``` - (instancetype _Nullable)initWithDefinition:(NSDictionary<NSString *,id> * _Nonnull)dict fromArchive:(BOOL)archived ``` |

Modified [-[AMAction logMessageWithLevel:format:]](https://developer.apple.com/documentation/automator/amaction/1438359-logmessagewithlevel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)logMessageWithLevel:(AMLogLevel)level format:(NSString *)format, ... ``` |
| To | ``` - (void)logMessageWithLevel:(AMLogLevel)level format:(NSString * _Nonnull)format, ... ``` |

Modified [AMAction.name](https://developer.apple.com/documentation/automator/amaction/1419648-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSString *name ``` |
| To | ``` @property(readonly, strong, nonnull) NSString *name ``` |

Modified [AMAction.output](https://developer.apple.com/documentation/automator/amaction/1419786-output)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id output ``` |
| To | ``` @property(strong, nullable) id output ``` |

Modified [-[AMAction runAsynchronouslyWithInput:]](https://developer.apple.com/documentation/automator/amaction/1419691-runasynchronouslywithinput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAsynchronouslyWithInput:(id)input ``` |
| To | ``` - (void)runAsynchronouslyWithInput:(id _Nullable)input ``` |

Modified [-[AMAction runWithInput:error:]](https://developer.apple.com/documentation/automator/amaction/1419624-run)

|  | Declaration |
| --- | --- |
| From | ``` - (id)runWithInput:(id)input error:(NSError **)error ``` |
| To | ``` - (id _Nullable)runWithInput:(id _Nullable)input error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[AMAction runWithInput:fromAction:error:]](https://developer.apple.com/documentation/automator/amaction/1438363-runwithinput)

|  | Declaration |
| --- | --- |
| From | ``` - (id)runWithInput:(id)input fromAction:(AMAction *)anAction error:(NSDictionary **)errorInfo ``` |
| To | ``` - (id _Nullable)runWithInput:(id _Nullable)input fromAction:(AMAction * _Nullable)anAction error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified [AMAction.selectedInputType](https://developer.apple.com/documentation/automator/amaction/1419756-selectedinputtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSString *selectedInputType ``` |
| To | ``` @property(strong, nullable) NSString *selectedInputType ``` |

Modified [AMAction.selectedOutputType](https://developer.apple.com/documentation/automator/amaction/1419661-selectedoutputtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSString *selectedOutputType ``` |
| To | ``` @property(strong, nullable) NSString *selectedOutputType ``` |

Modified [-[AMAction writeToDictionary:]](https://developer.apple.com/documentation/automator/amaction/1419736-writetodictionary)

|  | Declaration |
| --- | --- |
| From | ``` - (void)writeToDictionary:(NSMutableDictionary *)dictionary ``` |
| To | ``` - (void)writeToDictionary:(NSMutableDictionary<NSString *,id> * _Nonnull)dictionary ``` |

#### AMAppleScriptAction.h

Modified [AMAppleScriptAction.script](https://developer.apple.com/documentation/automator/amapplescriptaction/1419700-script)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) OSAScript *script ``` |
| To | ``` @property(strong, nonnull) OSAScript *script ``` |

#### AMBundleAction.h

Removed [-[AMBundleAction initWithDefinition:fromArchive:]](https://developer.apple.com/documentation/automator/ambundleaction/1807582-initwithdefinition)Modified [AMBundleAction.bundle](https://developer.apple.com/documentation/automator/ambundleaction/1419572-bundle)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSBundle *bundle ``` |
| To | ``` @property(readonly, strong, nonnull) NSBundle *bundle ``` |

Modified [AMBundleAction.parameters](https://developer.apple.com/documentation/automator/ambundleaction/1419634-parameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSMutableDictionary *parameters ``` |
| To | ``` @property(strong, nullable) NSMutableDictionary<NSString *,id> *parameters ``` |

Modified [AMBundleAction.view](https://developer.apple.com/documentation/automator/ambundleaction/1419665-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSView *view ``` |
| To | ``` @property(readonly, strong, nullable) NSView *view ``` |

#### AMShellScriptAction.h

Modified [AMShellScriptAction.inputFieldSeparator](https://developer.apple.com/documentation/automator/amshellscriptaction/1419760-inputfieldseparator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)inputFieldSeparator ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *inputFieldSeparator ``` |

Modified [AMShellScriptAction.outputFieldSeparator](https://developer.apple.com/documentation/automator/amshellscriptaction/1419636-outputfieldseparator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)outputFieldSeparator ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *outputFieldSeparator ``` |

Modified [AMShellScriptAction.remapLineEndings](https://developer.apple.com/documentation/automator/amshellscriptaction/1419681-remaplineendings)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)remapLineEndings ``` |
| To | ``` @property(readonly) BOOL remapLineEndings ``` |

#### AMWorkflow.h

Added [-[AMWorkflow init]](https://developer.apple.com/documentation/automator/amworkflow/1419602-init)Modified [AMWorkflow.actions](https://developer.apple.com/documentation/automator/amworkflow/1419646-actions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSArray *actions ``` |
| To | ``` @property(readonly, retain, nonnull) NSArray<__kindof AMAction *> *actions ``` |

Modified [-[AMWorkflow addAction:]](https://developer.apple.com/documentation/automator/amworkflow/1419708-addaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAction:(AMAction *)action ``` |
| To | ``` - (void)addAction:(AMAction * _Nonnull)action ``` |

Modified [AMWorkflow.fileURL](https://developer.apple.com/documentation/automator/amworkflow/1419726-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *fileURL ``` |
| To | ``` @property(readonly, copy, nullable) NSURL *fileURL ``` |

Modified [-[AMWorkflow initWithContentsOfURL:error:]](https://developer.apple.com/documentation/automator/amworkflow/1419774-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)fileURL error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)fileURL error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AMWorkflow.input](https://developer.apple.com/documentation/automator/amworkflow/1419587-input)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) id input ``` |
| To | ``` @property(readwrite, retain, nullable) id input ``` |

Modified [-[AMWorkflow insertAction:atIndex:]](https://developer.apple.com/documentation/automator/amworkflow/1419714-insertaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertAction:(AMAction *)action atIndex:(NSUInteger)index ``` |
| To | ``` - (void)insertAction:(AMAction * _Nonnull)action atIndex:(NSUInteger)index ``` |

Modified [AMWorkflow.output](https://developer.apple.com/documentation/automator/amworkflow/1419626-output)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id output ``` |
| To | ``` @property(readonly, retain, nullable) id output ``` |

Modified [-[AMWorkflow removeAction:]](https://developer.apple.com/documentation/automator/amworkflow/1419604-removeaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAction:(AMAction *)action ``` |
| To | ``` - (void)removeAction:(AMAction * _Nonnull)action ``` |

Modified [+[AMWorkflow runWorkflowAtURL:withInput:error:]](https://developer.apple.com/documentation/automator/amworkflow/1419750-runworkflowaturl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)runWorkflowAtURL:(NSURL *)fileURL withInput:(id)input error:(NSError **)error ``` |
| To | ``` + (id _Nullable)runWorkflowAtURL:(NSURL * _Nonnull)fileURL withInput:(id _Nullable)input error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[AMWorkflow setValue:forVariableWithName:]](https://developer.apple.com/documentation/automator/amworkflow/1419768-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setValue:(id)value forVariableWithName:(NSString *)variableName ``` |
| To | ``` - (BOOL)setValue:(id _Nullable)value forVariableWithName:(NSString * _Nonnull)variableName ``` |

Modified [-[AMWorkflow valueForVariableWithName:]](https://developer.apple.com/documentation/automator/amworkflow/1419622-valueforvariablewithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)valueForVariableWithName:(NSString *)variableName ``` |
| To | ``` - (id _Nonnull)valueForVariableWithName:(NSString * _Nonnull)variableName ``` |

Modified [-[AMWorkflow writeToURL:error:]](https://developer.apple.com/documentation/automator/amworkflow/1419685-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)writeToURL:(NSURL *)fileURL error:(NSError **)outError ``` |
| To | ``` - (BOOL)writeToURL:(NSURL * _Nonnull)fileURL error:(NSError * _Nullable * _Nullable)outError ``` |

#### AMWorkflowController.h

Modified [AMWorkflowController.delegate](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419724-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id delegate ``` |
| To | ``` @property(assign, nullable) id delegate ``` |

Modified [-[AMWorkflowController pause:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419659-pause)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)pause:(id)sender ``` |
| To | ``` - (IBAction)pause:(id _Nonnull)sender ``` |

Modified [-[AMWorkflowController reset:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419748-reset)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)reset:(id)sender ``` |
| To | ``` - (IBAction)reset:(id _Nonnull)sender ``` |

Modified [-[AMWorkflowController run:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419780-run)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)run:(id)sender ``` |
| To | ``` - (IBAction)run:(id _Nonnull)sender ``` |

Modified [-[AMWorkflowController step:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419740-step)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)step:(id)sender ``` |
| To | ``` - (IBAction)step:(id _Nonnull)sender ``` |

Modified [-[AMWorkflowController stop:]](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419712-stop)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)stop:(id)sender ``` |
| To | ``` - (IBAction)stop:(id _Nonnull)sender ``` |

Modified [AMWorkflowController.workflow](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419620-workflow)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) AMWorkflow *workflow ``` |
| To | ``` @property(strong, nullable) AMWorkflow *workflow ``` |

Modified [AMWorkflowController.workflowView](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419614-workflowview)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) AMWorkflowView *workflowView ``` |
| To | ``` @property(strong, nullable) AMWorkflowView *workflowView ``` |

Modified [-[NSObject workflowController:didError:]](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419652-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowController:(AMWorkflowController *)controller didError:(NSError *)error ``` |
| To | ``` - (void)workflowController:(AMWorkflowController * _Nonnull)controller didError:(NSError * _Nonnull)error ``` |

Modified [-[NSObject workflowController:didRunAction:]](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419675-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowController:(AMWorkflowController *)controller didRunAction:(AMAction *)action ``` |
| To | ``` - (void)workflowController:(AMWorkflowController * _Nonnull)controller didRunAction:(AMAction * _Nonnull)action ``` |

Modified [-[NSObject workflowController:willRunAction:]](https://developer.apple.com/documentation/objectivec/nsobject/1419720-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowController:(AMWorkflowController *)controller willRunAction:(AMAction *)action ``` |
| To | ``` - (void)workflowController:(AMWorkflowController * _Nonnull)controller willRunAction:(AMAction * _Nonnull)action ``` |

Modified [-[NSObject workflowControllerDidRun:]](https://developer.apple.com/documentation/objectivec/nsobject/1419762-workflowcontrollerdidrun)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowControllerDidRun:(AMWorkflowController *)controller ``` |
| To | ``` - (void)workflowControllerDidRun:(AMWorkflowController * _Nonnull)controller ``` |

Modified [-[NSObject workflowControllerDidStop:]](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419770-workflowcontrollerdidstop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowControllerDidStop:(AMWorkflowController *)controller ``` |
| To | ``` - (void)workflowControllerDidStop:(AMWorkflowController * _Nonnull)controller ``` |

Modified [-[NSObject workflowControllerWillRun:]](https://developer.apple.com/documentation/objectivec/nsobject/1419730-workflowcontrollerwillrun)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowControllerWillRun:(AMWorkflowController *)controller ``` |
| To | ``` - (void)workflowControllerWillRun:(AMWorkflowController * _Nonnull)controller ``` |

Modified [-[NSObject workflowControllerWillStop:]](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419598-workflowcontrollerwillstop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)workflowControllerWillStop:(AMWorkflowController *)controller ``` |
| To | ``` - (void)workflowControllerWillStop:(AMWorkflowController * _Nonnull)controller ``` |

#### AMWorkflowView.h

Modified [AMWorkflowView.workflowController](https://developer.apple.com/documentation/automator/amworkflowview/1419790-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) AMWorkflowController *workflowController ``` |
| To | ``` @property(strong, nullable) AMWorkflowController *workflowController ``` |

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

---
title: App intents
framework: App Intents
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/appintents/app-intents
source_url: 'https://developer.apple.com/documentation/appintents/app-intents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appintents/app-intents.json'
content_hash: 'sha256:1e7630d34f65e246'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [App Intents](../appintents.md)

# App intents

<sub>API Collection</sub>

Make your app’s custom actions available to the system by using app intent types.

## Overview

An app intent expresses one of your app’s capabilities to the system, and contains code to perform that action. You express your app intents as types that adopt the [AppIntent](appintent.md) protocol and specify the data you need to perform the action. For specific types of actions, you might also base your intents on other [app intent types](app-intent-types.md). For example, if your app intent launches your app and displays some content, use the [OpenIntent](openintent.md) protocol instead. If an app intent supports system features, adopt a schema from an [app schema domain](app-schema-domains.md).

If your app intent requires data to complete its action, specify those data requirements using parameters. An app intent parameter is a property that you annotate with the `@Parameter` macro. To improve the experience of specifying parameter values, include parameter summaries.

An intent returns a result to tell the system when it completes its action, and whether the action was successful or failed. A result can also provide textual or view-based content for Siri or the Shortcuts app to incorporate into conversations.

## Topics

### App intent definition

- [Creating your first app intent](creating-your-first-app-intent.md) — Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md) — Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Soup Chef with App Intents: Migrating custom intents](../sirikit/soup-chef-with-app-intents-migrating-custom-intents.md) — Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [AppIntent](appintent.md) — An interface you use to express app-specific actions and make them available to the rest of the system.
- [App intent types](app-intent-types.md) — Build your intents from types that define common behaviors such as opening or deleting items, playing or recording media, and more.

### Add-on behaviors

- [UndoableIntent](undoableintent.md) — An interface you use to register undoable actions in your app intent code.
- [CancellableIntent](cancellableintent.md) — An interface to support the graceful cancellation of your app intent’s task.
- [LongRunningIntent](longrunningintent.md) — An interface you use to extend the background execution time of an app intent that performs a long-running task.
- [PredictableIntent](predictableintent.md) — An interface that indicates the system can suggest the intent as a potential action to run.
- [IntentPrediction](intentprediction.md) — A prediction for an app intent that the system might display to someone when it’s relevant.

### Parameters

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md) — Enable people to configure app intents with their custom input values.
- [IntentParameter](intentparameter.md) — A property wrapper that indicates the associated property is an input argument of the app intent.
- [IntentParameterDependency](intentparameterdependency.md) — A property wrapper that represents an app intent dependency you use to provide dynamic options.
- [IntentParameterContext](intentparametercontext.md) — A type that provides information about an associated parameter during value resolution.
- [InputConnectionBehavior](inputconnectionbehavior.md) — Describes the input behaviors for connecting a parameter to the output of the previous App Intent.
- [DynamicOptionsProvider](dynamicoptionsprovider.md) — An interface for providing a dynamic list of options for a parameter of your app intent.
- [Resolvers](resolvers.md) — Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.

### Disambiguation

- [IntentChoiceOption](intentchoiceoption.md) — A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.
- [ConfirmationConditions](confirmationconditions.md) — Conditions for a confirmation request.

### Results

- [IntentResult](intentresult.md) — A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.
- [IntentDialog](intentdialog.md) — The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [IntentResultContainer](intentresultcontainer.md) — An object that represents the output of a completed intent.
- [ProvidesDialog](providesdialog.md) — The result of performing an action that delivers a dialog back to the initiator of the action.
- [ReturnsValue](returnsvalue.md) — The result of performing an action that delivers a value back to the initiator.
- [ShowsSnippetView](showssnippetview.md) — The result of performing an action that delivers a view back to the initiator of the action.
- [ResultsCollection](resultscollection.md) — A protocol representing a collection of returned items with support for sectioning.
- [OpensIntent](opensintent.md) — The result of performing an action that delivers an app intent back to the initiator of the action.

### Dependency management

- [AppDependencyManager](appdependencymanager.md) — An object that manages the registration and initialization of an app intent’s dependencies.
- [AppDependency](appdependency.md) — A property wrapper that resolves a registered dependency at runtime.

### Shortcuts support

- [ParameterSummary](parametersummary.md) — An interface for defining the visual representation of an app intent’s parameters.
- [IntentParameterSummary](intentparametersummary.md) — A type that describes the user interface configuration of an app intent’s parameters.
- [ParameterSummaryString](parametersummarystring.md) — A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.
- [ParameterSummaryWhenCondition](parametersummarywhencondition.md) — A type that represents a conditional statement in a parameter summary.
- [ParameterSummarySwitchCondition](parametersummaryswitchcondition.md) — A type that represents a switch statement in a parameter summary.
- [ParameterSummaryCaseCondition](parametersummarycasecondition.md) — A type that represents an individual case of a switch statement in a parameter summary.
- [ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md) — A type that represents the default case of a switch statement in a parameter summary.

### Intent-related data

- [IntentModes](intentmodes.md) — A set of options you use to configure the runtime behavior of an app intent.
- [IntentSystemContext](intentsystemcontext.md) — Contextual information that the system provides while it performs an app intent.
- [IntentDescription](intentdescription.md) — The human-readable description and metadata for an app intent.
- [IntentDialog](intentdialog.md) — The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [IntentDeprecation](intentdeprecation.md)
- [IntentProjection](intentprojection.md) — Projections for an app intent that returns non-optional values for parameters.

### Type conversions

- [IntentValueConvertible](intentvalueconvertible.md) — A protocol that allows the system to use types to as app intent parameters or properties.
- [IntentValueConvertibleWrapper](intentvalueconvertiblewrapper.md) — A protocol for types that wrap another intent value that supports conversion.
- [IntentValueExpressing](intentvalueexpressing.md) — A protocol for types that can create intent value expressions.

### Intent queries

- [IntentValueQuery](intentvaluequery.md) — A query that provides entity values to the system; for example, for visual intelligence search.
- [IntentValueContainer](intentvaluecontainer.md) — A container that stores a value that supports intent value conversion.
- [IntentValueExpression](intentvalueexpression.md) — A type that represents a lazily evaluated intent value.

## See Also

### App-specific content

- [App entities](app-entities.md) — Make your app’s core types and data concepts available to the system using app entity types.
- [App enums](app-enums.md) — Make your app’s enumerations and predefined values available to the system by using app enum types.
- [Common data types](common-data-types.md) — Use framework-defined types for common parameter and result data types such as contacts, files, currencies, and more.
- [App extension](app-extension.md) — Deliver app intents in an app extension or other package that lives outside your app’s code.

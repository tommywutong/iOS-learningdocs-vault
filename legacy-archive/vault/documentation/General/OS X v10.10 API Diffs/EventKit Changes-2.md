---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/EventKit.html
archived_at: '2026-07-15T07:34:54.271323Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# EventKit Changes

## EventKit (Added)

Added EKAlarmAdded EKAlarm.absoluteDateAdded EKAlarm.init(absoluteDate: NSDate!)Added EKAlarm.emailAddressAdded EKAlarm.proximityAdded EKAlarm.relativeOffsetAdded EKAlarm.init(relativeOffset: NSTimeInterval)Added EKAlarm.soundNameAdded EKAlarm.structuredLocationAdded EKAlarm.typeAdded EKAlarmType [struct]Added EKAlarmType.init(_: UInt32)Added EKAlarmType.valueAdded EKAuthorizationStatus [enum]Added EKAuthorizationStatus.AuthorizedAdded EKAuthorizationStatus.DeniedAdded EKAuthorizationStatus.NotDeterminedAdded EKAuthorizationStatus.RestrictedAdded EKCalendarAdded EKCalendar.allowedEntityTypesAdded EKCalendar.allowsContentModificationsAdded EKCalendar.calendarIdentifierAdded EKCalendar.colorAdded EKCalendar.init(forEntityType: EKEntityType, eventStore: EKEventStore!)Added EKCalendar.immutableAdded EKCalendar.sourceAdded EKCalendar.subscribedAdded EKCalendar.supportedEventAvailabilitiesAdded EKCalendar.titleAdded EKCalendar.typeAdded EKCalendarItemAdded EKCalendarItem.URLAdded EKCalendarItem.addAlarm(EKAlarm!)Added EKCalendarItem.addRecurrenceRule(EKRecurrenceRule!)Added EKCalendarItem.alarmsAdded EKCalendarItem.attendeesAdded EKCalendarItem.calendarAdded EKCalendarItem.calendarItemExternalIdentifierAdded EKCalendarItem.calendarItemIdentifierAdded EKCalendarItem.creationDateAdded EKCalendarItem.hasAlarmsAdded EKCalendarItem.hasAttendeesAdded EKCalendarItem.hasNotesAdded EKCalendarItem.hasRecurrenceRulesAdded EKCalendarItem.lastModifiedDateAdded EKCalendarItem.locationAdded EKCalendarItem.notesAdded EKCalendarItem.recurrenceRulesAdded EKCalendarItem.removeAlarm(EKAlarm!)Added EKCalendarItem.removeRecurrenceRule(EKRecurrenceRule!)Added EKCalendarItem.timeZoneAdded EKCalendarItem.titleAdded EKCalendarType [struct]Added EKCalendarType.init(_: UInt32)Added EKCalendarType.valueAdded EKErrorCode [struct]Added EKErrorCode.init(_: UInt32)Added EKErrorCode.valueAdded EKEventAdded EKEvent.allDayAdded EKEvent.availabilityAdded EKEvent.birthdayPersonUniqueIDAdded EKEvent.compareStartDateWithEvent(EKEvent!) -> NSComparisonResultAdded EKEvent.endDateAdded EKEvent.eventIdentifierAdded EKEvent.init(eventStore: EKEventStore!)Added EKEvent.isDetachedAdded EKEvent.occurrenceDateAdded EKEvent.organizerAdded EKEvent.refresh() -> BoolAdded EKEvent.startDateAdded EKEvent.statusAdded EKEventAvailability [struct]Added EKEventAvailability.init(_: Int32)Added EKEventAvailability.valueAdded EKEventStatus [struct]Added EKEventStatus.init(_: UInt32)Added EKEventStatus.valueAdded EKEventStoreAdded EKEventStore.init()Added EKEventStore.authorizationStatusForEntityType(EKEntityType) -> EKAuthorizationStatus [class]Added EKEventStore.calendarItemWithIdentifier(String!) -> EKCalendarItem!Added EKEventStore.calendarItemsWithExternalIdentifier(String!) -> [AnyObject]!Added EKEventStore.calendarWithIdentifier(String!) -> EKCalendar!Added EKEventStore.calendarsForEntityType(EKEntityType) -> [AnyObject]!Added EKEventStore.cancelFetchRequest(AnyObject!)Added EKEventStore.commit(NSErrorPointer) -> BoolAdded EKEventStore.defaultCalendarForNewEventsAdded EKEventStore.defaultCalendarForNewReminders() -> EKCalendar!Added EKEventStore.enumerateEventsMatchingPredicate(NSPredicate!, usingBlock: EKEventSearchCallback!)Added EKEventStore.eventStoreIdentifierAdded EKEventStore.eventWithIdentifier(String!) -> EKEvent!Added EKEventStore.eventsMatchingPredicate(NSPredicate!) -> [AnyObject]!Added EKEventStore.fetchRemindersMatchingPredicate(NSPredicate!, completion:(([AnyObject]!) -> Void)!) -> AnyObject!Added EKEventStore.predicateForCompletedRemindersWithCompletionDateStarting(NSDate!, ending: NSDate!, calendars:[AnyObject]!) -> NSPredicate!Added EKEventStore.predicateForEventsWithStartDate(NSDate!, endDate: NSDate!, calendars:[AnyObject]!) -> NSPredicate!Added EKEventStore.predicateForIncompleteRemindersWithDueDateStarting(NSDate!, ending: NSDate!, calendars:[AnyObject]!) -> NSPredicate!Added EKEventStore.predicateForRemindersInCalendars([AnyObject]!) -> NSPredicate!Added EKEventStore.refreshSourcesIfNecessary()Added EKEventStore.removeCalendar(EKCalendar!, commit: Bool, error: NSErrorPointer) -> BoolAdded EKEventStore.removeEvent(EKEvent!, span: EKSpan, commit: Bool, error: NSErrorPointer) -> BoolAdded EKEventStore.removeReminder(EKReminder!, commit: Bool, error: NSErrorPointer) -> BoolAdded EKEventStore.requestAccessToEntityType(EKEntityType, completion: EKEventStoreRequestAccessCompletionHandler!)Added EKEventStore.reset()Added EKEventStore.saveCalendar(EKCalendar!, commit: Bool, error: NSErrorPointer) -> BoolAdded EKEventStore.saveEvent(EKEvent!, span: EKSpan, commit: Bool, error: NSErrorPointer) -> BoolAdded EKEventStore.saveReminder(EKReminder!, commit: Bool, error: NSErrorPointer) -> BoolAdded EKEventStore.sourceWithIdentifier(String!) -> EKSource!Added EKEventStore.sources() -> [AnyObject]!Added EKObjectAdded EKObject.hasChanges() -> BoolAdded EKObject.isNew() -> BoolAdded EKObject.refresh() -> BoolAdded EKObject.reset()Added EKObject.rollback()Added EKParticipantAdded EKParticipant.ABPersonInAddressBook(ABAddressBook!) -> ABPerson!Added EKParticipant.URLAdded EKParticipant.isCurrentUserAdded EKParticipant.nameAdded EKParticipant.participantRoleAdded EKParticipant.participantStatusAdded EKParticipant.participantTypeAdded EKParticipantRole [struct]Added EKParticipantRole.init(_: UInt32)Added EKParticipantRole.valueAdded EKParticipantStatus [struct]Added EKParticipantStatus.init(_: UInt32)Added EKParticipantStatus.valueAdded EKParticipantType [struct]Added EKParticipantType.init(_: UInt32)Added EKParticipantType.valueAdded EKRecurrenceDayOfWeekAdded EKRecurrenceDayOfWeek.init(_: Int)Added EKRecurrenceDayOfWeek.init(_: Int, weekNumber: Int)Added EKRecurrenceDayOfWeek.dayOfTheWeekAdded EKRecurrenceDayOfWeek.init(dayOfTheWeek: Int, weekNumber: Int)Added EKRecurrenceDayOfWeek.weekNumberAdded EKRecurrenceEndAdded EKRecurrenceEnd.endDateAdded EKRecurrenceEnd.occurrenceCountAdded EKRecurrenceEnd.recurrenceEndWithEndDate(NSDate!) -> AnyObject! [class]Added EKRecurrenceEnd.recurrenceEndWithOccurrenceCount(Int) -> AnyObject! [class]Added EKRecurrenceFrequency [struct]Added EKRecurrenceFrequency.init(_: UInt32)Added EKRecurrenceFrequency.valueAdded EKRecurrenceRuleAdded EKRecurrenceRule.calendarIdentifierAdded EKRecurrenceRule.daysOfTheMonthAdded EKRecurrenceRule.daysOfTheWeekAdded EKRecurrenceRule.daysOfTheYearAdded EKRecurrenceRule.firstDayOfTheWeekAdded EKRecurrenceRule.frequencyAdded EKRecurrenceRule.intervalAdded EKRecurrenceRule.monthsOfTheYearAdded EKRecurrenceRule.recurrenceEndAdded EKRecurrenceRule.init(recurrenceWithFrequency: EKRecurrenceFrequency, interval: Int, daysOfTheWeek:[AnyObject]!, daysOfTheMonth:[AnyObject]!, monthsOfTheYear:[AnyObject]!, weeksOfTheYear:[AnyObject]!, daysOfTheYear:[AnyObject]!, setPositions:[AnyObject]!, end: EKRecurrenceEnd!)Added EKRecurrenceRule.init(recurrenceWithFrequency: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd!)Added EKRecurrenceRule.setPositionsAdded EKRecurrenceRule.weeksOfTheYearAdded EKReminderAdded EKReminder.completedAdded EKReminder.completionDateAdded EKReminder.dueDateComponentsAdded EKReminder.init(eventStore: EKEventStore!)Added EKReminder.priorityAdded EKReminder.startDateComponentsAdded EKReminderPriority [struct]Added EKReminderPriority.init(_: UInt)Added EKReminderPriority.valueAdded EKSourceAdded EKSource.calendarsForEntityType(EKEntityType) -> NSSet!Added EKSource.sourceIdentifierAdded EKSource.sourceTypeAdded EKSource.titleAdded EKSourceType [struct]Added EKSourceType.init(_: UInt32)Added EKSourceType.valueAdded EKSpan [struct]Added EKSpan.init(_: UInt32)Added EKSpan.valueAdded EKStructuredLocationAdded EKStructuredLocation.geoLocationAdded EKStructuredLocation.radiusAdded EKStructuredLocation.titleAdded EKStructuredLocation.init(title: String!)Added DATETIME_COMPONENTS_DO_NOT_USE()Added DATE_COMPONENTS_DO_NOT_USE()Added EKAlarmProximityAdded EKAlarmProximityEnterAdded EKAlarmProximityLeaveAdded EKAlarmProximityNoneAdded EKAlarmTypeAudioAdded EKAlarmTypeDisplayAdded EKAlarmTypeEmailAdded EKAlarmTypeProcedureAdded EKCalendarEventAvailabilityBusyAdded EKCalendarEventAvailabilityFreeAdded EKCalendarEventAvailabilityMaskAdded EKCalendarEventAvailabilityNoneAdded EKCalendarEventAvailabilityTentativeAdded EKCalendarEventAvailabilityUnavailableAdded EKCalendarTypeBirthdayAdded EKCalendarTypeCalDAVAdded EKCalendarTypeExchangeAdded EKCalendarTypeLocalAdded EKCalendarTypeSubscriptionAdded EKEntityMaskAdded EKEntityMaskEventAdded EKEntityMaskReminderAdded EKEntityTypeAdded EKEntityTypeEventAdded EKEntityTypeReminderAdded EKErrorAlarmGreaterThanRecurrenceAdded EKErrorAlarmProximityNotSupportedAdded EKErrorCalendarDoesNotAllowEventsAdded EKErrorCalendarDoesNotAllowRemindersAdded EKErrorCalendarHasNoSourceAdded EKErrorCalendarIsImmutableAdded EKErrorCalendarReadOnlyAdded EKErrorCalendarSourceCannotBeModifiedAdded EKErrorDatesInvertedAdded EKErrorDomainAdded EKErrorDurationGreaterThanRecurrenceAdded EKErrorEventNotMutableAdded EKErrorEventStoreNotAuthorizedAdded EKErrorInternalFailureAdded EKErrorInvalidEntityTypeAdded EKErrorInvalidSpanAdded EKErrorInvitesCannotBeMovedAdded EKErrorLastAdded EKErrorNoCalendarAdded EKErrorNoEndDateAdded EKErrorNoStartDateAdded EKErrorObjectBelongsToDifferentStoreAdded EKErrorPriorityIsInvalidAdded EKErrorProcedureAlarmsNotMutableAdded EKErrorRecurringReminderRequiresDueDateAdded EKErrorReminderLocationsNotSupportedAdded EKErrorSourceDoesNotAllowCalendarAddDeleteAdded EKErrorSourceDoesNotAllowEventsAdded EKErrorSourceDoesNotAllowRemindersAdded EKErrorStartDateCollidesWithOtherOccurrenceAdded EKErrorStartDateTooFarInFutureAdded EKErrorStructuredLocationsNotSupportedAdded EKEventAvailabilityBusyAdded EKEventAvailabilityFreeAdded EKEventAvailabilityNotSupportedAdded EKEventAvailabilityTentativeAdded EKEventAvailabilityUnavailableAdded EKEventSearchCallbackAdded EKEventStatusCanceledAdded EKEventStatusConfirmedAdded EKEventStatusNoneAdded EKEventStatusTentativeAdded EKEventStoreChangedNotificationAdded EKEventStoreRequestAccessCompletionHandlerAdded EKFridayAdded EKMondayAdded EKParticipantRoleChairAdded EKParticipantRoleNonParticipantAdded EKParticipantRoleOptionalAdded EKParticipantRoleRequiredAdded EKParticipantRoleUnknownAdded EKParticipantStatusAcceptedAdded EKParticipantStatusCompletedAdded EKParticipantStatusDeclinedAdded EKParticipantStatusDelegatedAdded EKParticipantStatusInProcessAdded EKParticipantStatusPendingAdded EKParticipantStatusTentativeAdded EKParticipantStatusUnknownAdded EKParticipantTypeGroupAdded EKParticipantTypePersonAdded EKParticipantTypeResourceAdded EKParticipantTypeRoomAdded EKParticipantTypeUnknownAdded EKRecurrenceFrequencyDailyAdded EKRecurrenceFrequencyMonthlyAdded EKRecurrenceFrequencyWeeklyAdded EKRecurrenceFrequencyYearlyAdded EKReminderPriorityHighAdded EKReminderPriorityLowAdded EKReminderPriorityMediumAdded EKReminderPriorityNoneAdded EKSaturdayAdded EKSourceTypeBirthdaysAdded EKSourceTypeCalDAVAdded EKSourceTypeExchangeAdded EKSourceTypeLocalAdded EKSourceTypeMobileMeAdded EKSourceTypeSubscribedAdded EKSpanFutureEventsAdded EKSpanThisEventAdded EKSundayAdded EKThursdayAdded EKTuesdayAdded EKWednesdayAdded EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()

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

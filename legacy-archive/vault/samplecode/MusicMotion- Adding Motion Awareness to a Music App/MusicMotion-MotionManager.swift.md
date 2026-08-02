---
title: 'MusicMotion: Adding Motion Awareness to a Music App'
apple_id: TP40016160
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/MusicMotion/Listings/MusicMotion_MotionManager_swift.html
archived_at: '2026-07-18T03:16:32.807676Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MusicMotion: Adding Motion Awareness to a Music App](MusicMotion-%20Adding%20Motion%20Awareness%20to%20a%20Music%20App.md)


[Next](MusicMotion-SongViewController.swift.md)[Previous](MusicMotion-HistoryViewController.swift.md)

# MusicMotion/MotionManager.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This class manages the CoreMotion interactions and provides a delegate to indicate changes in context.
*/

import Foundation
import CoreMotion

/**
    `MotionContext` describes the user's current motion activity level. The higher
    the intensity, the more active the user is. Driving is handled seperately because
    the user's activity level is not directly not applicable while driving.
*/
enum MotionContext: String, CustomStringConvertible {
    case LowIntensity = "Low Intensity"
    case MediumIntensity = "Medium Intensity"
    case HighIntensity = "High Intensity"
    case Driving = "Driving"

    // MARK: CustomStringConvertible

    var description: String {
        return self.rawValue
    }
}

/**
    `MotionContextDelegate` exists to inform delegates of motion context changes.
    These contexts can be used to enable motion aware application specific behavior.
*/
protocol MotionContextDelegate: class {
    func lowIntensityContextStarted(_ manager: MotionManager)
    func mediumIntensityContextStarted(_ manager: MotionManager)
    func highIntensityContextStarted(_ manager: MotionManager)
    func drivingContextStarted(_ manager: MotionManager)
    func didEncounterAuthorizationError(_ manager: MotionManager)
}

/// These constants are application specific and should be tuned for your specific needs.
class MotionManager {
    // MARK: Static Properties

    static let maxActivitySamples = 2

    // 18 minutes per mile in meters per second.
    static let mediumPace = 0.671080

    // 12 minutes per mile in meters per second.
    static let highPace = 0.447387

    static let maxAltitudeSamples = 10

    static let metersForSignificantAltitudeChange = 5.0

    static let maxPedometerSamples = 1

    // MARK: Properties

    weak var delegate: MotionContextDelegate?

    var currentContext = MotionContext.LowIntensity

    let motionQueue: OperationQueue = {
        let motionQueue = OperationQueue()

        motionQueue.name = "com.example.apple-samplecode.MusicMotion"

        return motionQueue
    }()

    var recentActivities = [Activity]()

    let activityManager = CMMotionActivityManager()

    var recentMotionActivities = [CMMotionActivity]()

    let pedometer = CMPedometer()

    var recentPedometerData = [CMPedometerData]()

    let altimeter = CMAltimeter()

    var recentAlitudeData = [CMAltitudeData]()

    var isInHighIntensityContext: Bool {
        return ( isUserPaceHigh && isUserRunning ) || hasAltitudeChangedRecently
    }

    var isInMediumIntensityContext: Bool {
        return isUserPaceMedium && isUserWalking
    }

    var isInLowIntensityContext: Bool {
        return isUserStationary
    }

    var isInDrivingContext: Bool {
        return isUserDriving
    }

    // MARK: Live Activity Updates

    /**
        This function is the entry point for the motion context logic. This function
        fuses together activity updates and pedometer data to infer the user's
        activity level.
    */
    func startMonitoring() {
        // If activity updates are supported, start updates on the motionQueue.
        if CMMotionActivityManager.isActivityAvailable() {
            activityManager.startActivityUpdates(to: motionQueue) { activity in
                // Ignore unclassified activites.
                guard let activity = activity , activity.hasActivitySignature else { return }

                self.saveMotionActivity(activity)
                self.updateUserContext()
            }
        }
        else {
            print("Activity updates are not available.")
        }

        // If step counting is available, start pedometer updates from now forward.
        if CMPedometer.isStepCountingAvailable() {
            let now = Date()

            pedometer.startUpdates(from: now) { pedometerData, error in
                if let pedometerData = pedometerData {
                    self.savePedometerData(pedometerData)
                    self.updateUserContext()
                }
                else if let error = error {
                    self.handleError(error as NSError)
                }
            }
        }
        else {
            print("Step counting is not available.")
        }
    }

    // MARK: Context Decision Logic

    func updateUserContext() {
        // If the user is running or walking, enable altitude updates to record elevation changes.
        if isUserRunning || isUserWalking {
            if CMAltimeter.isRelativeAltitudeAvailable() {
                altimeter.startRelativeAltitudeUpdates(to: motionQueue) { altitudeData, error in
                    if let altitudeData = altitudeData {
                        self.saveAltitudeData(altitudeData)
                        self.updateUserContext()
                    }
                    else if let error = error {
                        self.handleError(error as NSError)
                    }
                }
            }
            else {
                print("Relative altitude is not available.")
            }
        }
        else if CMAltimeter.isRelativeAltitudeAvailable() {
            altimeter.stopRelativeAltitudeUpdates()
        }

        updateContextAndNotifyDelegate()
    }

    func updateContextAndNotifyDelegate() {
        // Only invoke the delegate if we see a change in intensity.
        if currentContext != .Driving && isInDrivingContext {
            currentContext = .Driving
            delegate?.drivingContextStarted(self)
        }
        else if currentContext != .LowIntensity && isInLowIntensityContext {
            currentContext = .LowIntensity
            delegate?.lowIntensityContextStarted(self)
        }
        else if currentContext != .MediumIntensity && isInMediumIntensityContext {
            self.currentContext = .MediumIntensity
            delegate?.mediumIntensityContextStarted(self)
        }

        else if currentContext != .HighIntensity && isInHighIntensityContext {
            currentContext = .HighIntensity
            delegate?.highIntensityContextStarted(self)
        }
    }

    // MARK: Context Decision Functions

    func activitesMatch(_ test: (CMMotionActivity) -> Bool) -> Bool {
        if recentMotionActivities.isEmpty { return false }

        // Only return true if every activity passes the test closure.
        return !recentMotionActivities.contains { !test($0) }
    }

    // Confidence could be incorporated in the isUser functions to trade accuracy with responsiveness.
    var isUserRunning: Bool {
        return activitesMatch { $0.running }
    }

    var isUserStationary: Bool {
        return activitesMatch { $0.stationary }
    }

    var isUserWalking: Bool {
        return activitesMatch { $0.walking }
    }

    var isUserDriving: Bool {
        return activitesMatch { $0.automotive }
    }

    var hasAltitudeChangedRecently: Bool {
        guard let lastAltitude = recentAlitudeData.last?.relativeAltitude,
                  let firstAltitude = recentAlitudeData.first?.relativeAltitude else {
            return false
        }

        return fabs(firstAltitude.doubleValue - lastAltitude.doubleValue) > MotionManager.metersForSignificantAltitudeChange
    }

    var isUserPaceHigh: Bool {
        let pace = currentPace

        /*
            Avoid pace comparision if pace is unavailable. This will making running
            the only determination for high intensity.
        */
        if pace == 0 { return true }

        // Return true if we are faster than the high pace.
        return pace < MotionManager.highPace
    }

    var isUserPaceMedium: Bool {
        let pace = currentPace

        /*
            Avoid pace comparision if pace is unavailable. This will making walking 
            the only determination for medium intensity.
        */
        if pace == 0 { return true }

        /*
            Return true if we are faster than the medium pace and but slower than
            the high pace.
        */
        return pace < MotionManager.mediumPace && pace > MotionManager.highPace
    }

    // The faster the user is moving the lower the pace value.
    var currentPace: Double {
        // If pace is not available then return.
        guard let pace = recentPedometerData.first?.currentPace?.doubleValue else { return 0 }

        return pace
    }

    //MARK: Recent Activity Processing

    func filterActivites(_ activities: [CMMotionActivity]) -> [CMMotionActivity] {
        // Filter out unknown activity, stationary activity, and low confidence activity.
        return activities.filter { activity in
            return activity.hasActivitySignature &&
                   !activity.stationary &&
                   activity.confidence.rawValue > CMMotionActivityConfidence.low.rawValue
        }
    }

    /// A convenience type to use as the return value to `findActivitySegments(_:)`.
    typealias ActivitySegment = (activity: CMMotionActivity, endDate: Date)

    func findActivitySegments(_ activities: [CMMotionActivity]) -> [ActivitySegment] {
        var segments = [ActivitySegment]()

        var i = 0
        while i < activities.count - 1 {
            let activity = activities[i]
            let startDate = activity.startDate

            /*
                If the next nearest activity is the same and was within 60 minutes,
                consolidate the events together.
            */
            i += 1
            var nextActivity = activities[i]
            var endDate = nextActivity.startDate

            while i < activities.count - 1 {
                /*
                    Once both activities are not the same, we have reached the end 
                    of our current activity.
                */
                if !activity.isSimilarToActivity(nextActivity) {
                    break
                }

                /*
                    Make sure the previous matching activity was within 60 minutes.
                    After 60 minutes we will call that a separate activity. Ex: Walking,
                    Stationary (60 mins), Walking will become two seperate Walking
                    activities.
                */
                let previousActivityEnd = activities[i - 1].startDate

                let secondsBetweenActivites = endDate.timeIntervalSince(previousActivityEnd)

                if secondsBetweenActivites >= 60 * 60 {
                    break
                }

                i += 1
                nextActivity = activities[i]
                endDate = nextActivity.startDate
            }

            /*
                Since we exit the loop we longer match activities, move back one
                position to the last match.
            */
            if i != activities.count - 1 {
                i -= 1
                nextActivity = activities[i]
            }
            else {
                /*
                    If we are at the end of the activities, treat the user as if
                    they are in the same activity still.
                */
                nextActivity = activities[i]
            }
            endDate = nextActivity.startDate

            /*
                If the total activity duration was longer than a minute, create an
                `ActivitySegment`.
            */
            if endDate.timeIntervalSince(startDate) > 60 {
                let activitySegment = ActivitySegment(activity, endDate)

                segments.append(activitySegment)
            }

            // Incrememnt the counter for the next loop.
            i += 1
        }

        return segments
    }

    func createActivityDataWithActivities(_ activities: [CMMotionActivity], completionHandler: @escaping (Void) -> Void) -> [Activity] {
        var results = [Activity]()

        /*
            This group is used to ensure all of the queries finish before we invoke 
            our `completionHandler`.
        */
        let group = DispatchGroup()

        // Serialization queue for result array.
        let queue = DispatchQueue(label: "com.example.apple-samplecode.com.resultQueue", attributes: [])

        /*
            First, filter activity data that does not have a signature, is low
            confidence, or is stationary.
        */
        let filteredActivities = filterActivites(activities)

        /*
            Next, find the periods of time between each signifcant activity segment
            to query for pedometer data.
        */
        let activitySegments = findActivitySegments(filteredActivities)

        for (activity, endDate) in activitySegments {
            group.enter()

            pedometer.queryPedometerData(from: activity.startDate, to: endDate) { pedometerData, error in
                queue.async {
                    let activity = Activity(activity: activity, startDate: activity.startDate, endDate: endDate, pedometerData: pedometerData)

                    results += [activity]
                }

                if let error = error {
                    self.handleError(error as NSError)
                }

                group.leave()
            }
        }

        group.notify(queue: DispatchQueue.main) {
            queue.sync {
                self.recentActivities = results.reversed()

                completionHandler()
            }
        }

        return results
    }

    // MARK: Historical Queries

    func queryForRecentActivityData(_ completionHandler: @escaping (Void) -> Void) {
        let now = Date()

        let dateComponents: DateComponents = {
            var dateComponents = DateComponents()
            dateComponents.setValue(-7, for: .day)
            return dateComponents
        }()

        guard let startDate = NSCalendar.current.date(byAdding: dateComponents, to: now) else { return }

        activityManager.queryActivityStarting(from: startDate, to: now, to: motionQueue) { activities, error in
            if let activities = activities {
                _ = self.createActivityDataWithActivities(activities, completionHandler:completionHandler)
            }
            else if let error = error {
                self.handleError(error as NSError)
            }
        }
    }

    // MARK: Data Management

    func savePedometerData(_ pedometerData: CMPedometerData) {
        recentPedometerData.insert(pedometerData, at: 0)

        if recentPedometerData.count > MotionManager.maxPedometerSamples {
            recentPedometerData.removeLast()
        }
    }

    func saveAltitudeData(_ altitude: CMAltitudeData) {
        recentAlitudeData.insert(altitude, at: 0)

        if recentAlitudeData.count > MotionManager.maxAltitudeSamples {
            recentAlitudeData.removeLast()
        }
    }

    func saveMotionActivity(_ activity: CMMotionActivity) {
        recentMotionActivities.insert(activity, at: 0)

        // Expire samples older than 60 seconds.
        let secondsToExpireActivity: TimeInterval = 1 * 60

        recentMotionActivities = recentMotionActivities.filter { activity in
            let secondsElapsed = Date().timeIntervalSince(activity.startDate)

            return secondsElapsed <= secondsToExpireActivity
        }

        // Remove the oldest element once we exceed our maximum sample count.
        if recentMotionActivities.count > MotionManager.maxActivitySamples {
            recentMotionActivities.removeLast()
        }
    }

    // MARK: Handling Authorization and Errors

    func handleError(_ error: NSError) {
        if error.code == Int(CMErrorMotionActivityNotAuthorized.rawValue) {
            delegate?.didEncounterAuthorizationError(self)
        }
        else {
            print(error)
        }
    }
}

extension CMMotionActivity {
    func isSimilarToActivity(_ activity: CMMotionActivity) -> Bool {
        // If we have multiple states set in an activity this will indicate a match on the first one.
        return walking && activity.walking ||
               running && activity.running ||
               automotive && activity.automotive ||
               cycling && activity.cycling ||
               stationary && activity.stationary
    }

    var hasActivitySignature: Bool {
        return walking || running || automotive || cycling || stationary
    }
}
```

[Next](MusicMotion-SongViewController.swift.md)[Previous](MusicMotion-HistoryViewController.swift.md)


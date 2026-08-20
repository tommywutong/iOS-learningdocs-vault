---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Galaxy_NBodySimulationDataGalaxy_h.html
archived_at: '2026-07-18T03:17:39.561671Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Galaxy-NBodySimulationDataGalaxy.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-CPU-NBodySimulationCPU.h.md)

# Sources/Model/NBody/Simulation/Core/Data/Galaxy/NBodySimulationDataGalaxy.h

```objc
/*
 <codex>
 <abstract>
 Functor for generating random packed data sets for the cpu or gpu bound simulator.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_DATA_GALAXY_H_
#define _NBODY_SIMULATION_DATA_GALAXY_H_

#import "CFDataFile.h"

#import "NBodySimulationProperties.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            class Galaxy
            {
            public:
                // Acquire the galaxy file using properties
                Galaxy(const size_t nParticles = 16384);

                // Copy constructor for deep-copy
                Galaxy(const Galaxy& rGalaxy);

                // Delete the object
                virtual ~Galaxy();

                // Assignment operator for deep object copy
                Galaxy& operator=(const Galaxy& rGalaxy);

                // End-of-File
                const bool eof() const;

                // Row count
                const size_t rows() const;

                // Column count
                const size_t columns() const;

                // File length, or the number of bytes
                const size_t length()  const;

                // Current line
                const size_t line() const;

                // Float vector from a line in the data file
                std::vector<float> floats();

                // Double vector from a line in the data file
                std::vector<double> doubles();

                // Reset the file content pointer to the beginning, past the header
                void reset();

            private:
                CF::DataFile* create(const size_t& nParticles);

            private:
                size_t        mnParticles;
                CF::DataFile* mpData;
            }; // Galaxy
        } // Data
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Galaxy-NBodySimulationDataGalaxy.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-CPU-NBodySimulationCPU.h.md)


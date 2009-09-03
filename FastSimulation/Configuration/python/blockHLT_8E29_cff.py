# /dev/CMSSW_3_3_0/pre1/8E29/V12 (CMSSW_3_3_X_2009-09-01-0500_HLT1)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_3_3_0/pre1/8E29/V12')
)


block_hltL1NonIsoLargeWindowElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.3 ),
  OrderedHitsFactoryPSet = cms.PSet( 
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "MixedLayerPairs" ),
    useOnDemandTracker = cms.untracked.int32( 0 )
  ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.045 ),
  PhiMin2 = cms.double( -0.01 ),
  LowPtThreshold = cms.double( 3.0 ),
  RegionPSet = cms.PSet( 
    deltaPhiRegion = cms.double( 0.4 ),
    originHalfLength = cms.double( 15.0 ),
    useZInVertex = cms.bool( True ),
    deltaEtaRegion = cms.double( 0.1 ),
    ptMin = cms.double( 1.5 ),
    originRadius = cms.double( 0.2 ),
    VertexProducer = cms.InputTag( "dummyVertices" )
  ),
  maxHOverE = cms.double( 999999.0 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.03 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.2 ),
  PhiMax2 = cms.double( 0.01 ),
  preFilteredSeeds = cms.bool( True ),
  r2MaxF = cms.double( 0.3 ),
  pPhiMin1 = cms.double( -0.03 ),
  initialSeeds = cms.InputTag( "noSeedsHere" ),
  pPhiMax1 = cms.double( 0.045 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 3.0 ),
  z2MaxB = cms.double( 0.2 ),
  fromTrackerSeeds = cms.bool( True ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  z2MinB = cms.double( -0.2 ),
  hbheInstance = cms.string( "" ),
  rMinI = cms.double( -0.2 ),
  hOverEConeSize = cms.double( 0.0 ),
  hOverEHBMinE = cms.double( 999999.0 ),
  hOverEHFMinE = cms.double( 999999.0 ),
  nSigmasDeltaZ1 = cms.double( 5.0 )
)
block_hltL1IsoLargeWindowElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.3 ),
  OrderedHitsFactoryPSet = cms.PSet( 
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "MixedLayerPairs" ),
    useOnDemandTracker = cms.untracked.int32( 0 )
  ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.045 ),
  PhiMin2 = cms.double( -0.01 ),
  LowPtThreshold = cms.double( 3.0 ),
  RegionPSet = cms.PSet( 
    deltaPhiRegion = cms.double( 0.4 ),
    originHalfLength = cms.double( 15.0 ),
    useZInVertex = cms.bool( True ),
    deltaEtaRegion = cms.double( 0.1 ),
    ptMin = cms.double( 1.5 ),
    originRadius = cms.double( 0.2 ),
    VertexProducer = cms.InputTag( "dummyVertices" )
  ),
  maxHOverE = cms.double( 999999.0 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.03 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.2 ),
  PhiMax2 = cms.double( 0.01 ),
  preFilteredSeeds = cms.bool( True ),
  r2MaxF = cms.double( 0.3 ),
  pPhiMin1 = cms.double( -0.03 ),
  initialSeeds = cms.InputTag( "noSeedsHere" ),
  pPhiMax1 = cms.double( 0.045 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 3.0 ),
  z2MaxB = cms.double( 0.2 ),
  fromTrackerSeeds = cms.bool( True ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  z2MinB = cms.double( -0.2 ),
  hbheInstance = cms.string( "" ),
  rMinI = cms.double( -0.2 ),
  hOverEConeSize = cms.double( 0.0 ),
  hOverEHBMinE = cms.double( 999999.0 ),
  hOverEHFMinE = cms.double( 999999.0 ),
  nSigmasDeltaZ1 = cms.double( 5.0 )
)
block_hltL1NonIsoStartUpElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.08 ),
  OrderedHitsFactoryPSet = cms.PSet( 
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "MixedLayerPairs" ),
    useOnDemandTracker = cms.untracked.int32( 0 )
  ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.035 ),
  PhiMin2 = cms.double( -0.0050 ),
  LowPtThreshold = cms.double( 3.0 ),
  RegionPSet = cms.PSet( 
    deltaPhiRegion = cms.double( 0.4 ),
    originHalfLength = cms.double( 15.0 ),
    useZInVertex = cms.bool( True ),
    deltaEtaRegion = cms.double( 0.1 ),
    ptMin = cms.double( 1.5 ),
    originRadius = cms.double( 0.2 ),
    VertexProducer = cms.InputTag( "dummyVertices" )
  ),
  maxHOverE = cms.double( 999999.0 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.025 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.11 ),
  PhiMax2 = cms.double( 0.0050 ),
  preFilteredSeeds = cms.bool( True ),
  r2MaxF = cms.double( 0.08 ),
  pPhiMin1 = cms.double( -0.025 ),
  initialSeeds = cms.InputTag( "noSeedsHere" ),
  pPhiMax1 = cms.double( 0.035 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 3.0 ),
  z2MaxB = cms.double( 0.05 ),
  fromTrackerSeeds = cms.bool( True ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  z2MinB = cms.double( -0.05 ),
  hbheInstance = cms.string( "" ),
  rMinI = cms.double( -0.11 ),
  hOverEConeSize = cms.double( 0.0 ),
  hOverEHBMinE = cms.double( 999999.0 ),
  hOverEHFMinE = cms.double( 999999.0 ),
  nSigmasDeltaZ1 = cms.double( 5.0 )
)
block_hltL1IsoStartUpElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.08 ),
  OrderedHitsFactoryPSet = cms.PSet( 
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "MixedLayerPairs" ),
    useOnDemandTracker = cms.untracked.int32( 0 )
  ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.035 ),
  PhiMin2 = cms.double( -0.0050 ),
  LowPtThreshold = cms.double( 3.0 ),
  RegionPSet = cms.PSet( 
    deltaPhiRegion = cms.double( 0.4 ),
    originHalfLength = cms.double( 15.0 ),
    useZInVertex = cms.bool( True ),
    deltaEtaRegion = cms.double( 0.1 ),
    ptMin = cms.double( 1.5 ),
    originRadius = cms.double( 0.2 ),
    VertexProducer = cms.InputTag( "dummyVertices" )
  ),
  maxHOverE = cms.double( 999999.0 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.025 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.11 ),
  PhiMax2 = cms.double( 0.0050 ),
  preFilteredSeeds = cms.bool( True ),
  r2MaxF = cms.double( 0.08 ),
  pPhiMin1 = cms.double( -0.025 ),
  initialSeeds = cms.InputTag( "noSeedsHere" ),
  pPhiMax1 = cms.double( 0.035 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 3.0 ),
  z2MaxB = cms.double( 0.05 ),
  fromTrackerSeeds = cms.bool( True ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  z2MinB = cms.double( -0.05 ),
  hbheInstance = cms.string( "" ),
  rMinI = cms.double( -0.11 ),
  hOverEConeSize = cms.double( 0.0 ),
  hOverEHBMinE = cms.double( 999999.0 ),
  hOverEHFMinE = cms.double( 999999.0 ),
  nSigmasDeltaZ1 = cms.double( 5.0 )
)

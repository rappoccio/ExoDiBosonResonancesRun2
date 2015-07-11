import FWCore.ParameterSet.Config as cms

import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt

hltFilter = hlt.triggerResultsFilter.clone(
                triggerConditions = ( 'HLT_Ele105_CaloIdVT_GsfTrkIdT_v*', 'HLT_Mu45_eta2p1_v*' ),
                #triggerConditions = ( 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v*', 'HLT_Mu30_TkMu11_v*' ),
                hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                l1tResults = cms.InputTag( "gtDigis" ),
                throw = False )

hltSequence = cms.Sequence( hltFilter )
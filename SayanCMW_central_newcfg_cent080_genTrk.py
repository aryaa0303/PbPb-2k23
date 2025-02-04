import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_pp_on_PbPb_2023_cff import Run3_pp_on_PbPb_2023 
#from Configuration.Eras.Era_Run3_pp_on_PbPb_approxSiStripClusters_2023_cff import Run3_pp_on_PbPb_approxSiStripClusters_2023 
process = cms.Process("SayanCMW")
#process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('MergingProducer.generalAndHiPixelTracks.MergingPixAndGenProducer_cfi')

# __________________ General _________________

# Configure the logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
)

# Configure the number of maximum event the analyser run on in interactive mode
# -1 == ALL
process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(100) 
#    input = cms.untracked.int32(500) 
)

#rootFiles = open("/eos/cms/store/group/phys_heavyions/sayan/TrackingTools_run3_datataking/pbpb_miniaod_datasets/run374810_ls0001_ls1752_streamPhysicsHIPhysicsRawPrime0_miniaod.txt", "r").readlines()
process.source = cms.Source("PoolSource",                                                                                
 #   duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),                                                       
    fileNames = cms.untracked.vstring(                                                                                   
#        'file:/eos/cms/store/group/phys_heavyions/wangj/RECO2023/miniaod_PhysicsHIPhysicsRawPrime0_374810/reco_run374810_ls0210_streamPhysicsHIPhysicsRawPrime0_StorageManager.root'
#       '/store/hidata/HIRun2023A/HIPhysicsRawPrime3/MINIAOD/PromptReco-v1/000/373/870/00000/6f2a145d-d79c-40d5-909d-174d860bde96.root'
#        '/store/hidata/HIRun2023A/HIMinimumBias0/MINIAOD/PromptReco-v1/000/373/870/00000/27122bd1-d3bf-4528-804d-013fd2fd7474.root'
        #'/store/hidata/HIRun2023A/HIPhysicsRawPrime0/MINIAOD/PromptReco-v2/000/374/668/00000/1bb772f3-bfa5-46ef-81d2-8cf78de992b0.root'
     #   '/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_1.root'
        '/store/mc/HINPbPbSpring23MiniAOD/MinBias_Drum5F_5p36TeV_hydjet/MINIAODSIM/NoPU_132X_mcRun3_2023_realistic_HI_v9-v2/2820000/02288831-b588-4380-bac8-9910f24691bd.root'
       # '/store/mc/HINPbPbSpring23MiniAOD/MinBias_Drum5F_5p36TeV_hydjet/MINIAODSIM/NoPU_132X_mcRun3_2023_realistic_HI_v9-v2/2820000/03f9d7b4-d340-47e0-9cf7-ce3596e0fc8c.root'
       # '/store/mc/HINPbPbSpring23MiniAOD/MinBias_HIJING_PbPb_2023_5p36TeV/MINIAODSIM/NoPU_132X_mcRun3_2023_realistic_HI_v9-v2/2810000/02164e27-2183-47fd-b7e7-ba1fc298ff72.root'
      #  '/store/mc/HINPbPbSpring23MiniAOD/MinBias_HIJING_PbPb_2023_5p36TeV/MINIAODSIM/NoPU_132X_mcRun3_2023_realistic_HI_v9-v2/2810000/02164e27-2183-47fd-b7e7-ba1fc298ff72.root'
        #        rootFiles
    ),                                                                                                                   
)                                                                                                                        

#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
# Set the global tag
from Configuration.AlCa.GlobalTag import GlobalTag                                                                       
#process.GlobalTag = GlobalTag(process.GlobalTag, '132X_dataRun3_Prompt_v7', '')                                         
#process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag                                                      
process.GlobalTag = GlobalTag(process.GlobalTag, '132X_mcRun3_2023_realistic_HI_v9', '')

#process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")                                           
#process.GlobalTag.toGet.extend([cms.PSet(record = cms.string("HeavyIonRcd"),
 #            tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5F_v1302x04_RECODEBUG_MC2023"),        
           #  tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289"),            
           #  connect = cms.string("sqlite_file:CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289.db"),   
            # connect = cms.string("sqlite_file:/afs/cern.ch/work/n/nsaha/public/for_GO/DBfile/Run3_DB/CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289.db"), 
  #           connect = cms.string("sqlite_file:CentralityTable_HFtowers200_HydjetDrum5F_v1302x04_RECODEBUG_MC2023.db"), 
   #          label = cms.untracked.string("HFtowers")                                                                         
   # ),           
#])                                                                                                                   
                                                                                                                  
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")                                                               
process.centralityBin.Centrality = cms.InputTag("hiCentrality")                                                          
process.centralityBin.centralityVariable = cms.string("HFtowers")                                                        
# __________________ Event selection _________________
# Add PbPb collision event selection 
#process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.load('HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzer_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hffilter_cfi')

#process.ana_step = cms.Path(process.offlinePrimaryVerticesRecovery + process.HiForest)
# Define the event selection sequence
process.eventFilter_HM = cms.Sequence(
    process.phfCoincFilter2Th4 *
#    process.phfCoincFilter3Th3 *
    process.primaryVertexFilter *
    process.clusterCompatibilityFilter
)
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '/eos/cms/store/group/phys_heavyions/sayan/HIN_run3_pseudo_JSON/HIPhysicsRawPrime/Golden_Online_live.json').getVLuminosityBlockRange()
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel  
process.hltfilter = hltHighLevel.clone(                         
    HLTPaths = [                                                
#        "HLT_HIMinimumBiasHF1ANDZDC2nOR_v*"
        "HLT_HIMinimumBiasHF1AND*"
        #"HLT_HIMinimumBiasHF1AND_v*"
#        "HLT_HIL1_UCC_0_1_v3"

    ]                                                           
)                                                               
# Define the output
process.TFileService = cms.Service("TFileService",fileName = cms.string('pbpb_2023_vn.root'))

process.load("Analyzers.SayanCMW.SayanCMW_cfi")
process.defaultCPDC.vertex = 'offlineSlimmedPrimaryVertices'
process.defaultCPDC.nonsym = False  ##Set True if you want non-symmetric filling C2 correlation
process.defaultCPDC.genTrk = True  ##It will be always True when running general tracks
process.defaultCPDC.genAndHiPixTrk = False  ##It will be always False when running general tracks

process.defaultCPDC.ptmin_trigg = 0.5       # Should not be less than 0.5 for genTrk
process.defaultCPDC.ptmax_trigg = 3.0
process.defaultCPDC.ptmin_ass = 0.5         # Should not be less than 0.5 for genTrk
process.defaultCPDC.ptmax_ass = 3.0
## Important : trigger_ptbin should be equal to associate_ptbin
process.defaultCPDC.trigger_ptbin = cms.untracked.vdouble(0.5,3.0)   ##trigger_ptbin[0] = ptmin_trigg   ##trigger_ptbin[trigger_ptbin.size() -1] = ptmax_trigg   
process.defaultCPDC.associate_ptbin = cms.untracked.vdouble(0.5,3.0)  ##associate_ptbin[0] = ptmin_ass   ##associate_ptbin[associate_ptbin.size() -1] = ptmax_ass


process.load("Analyzers.SayanCMW.SayanCMW_cff")

process.defaultAnalysis_05     = process.CPDC05.clone()
process.defaultAnalysis_510    = process.CPDC510.clone()

process.defaultAnalysis_1020   = process.CPDC1020.clone()
process.defaultAnalysis_2030   = process.CPDC2030.clone()
process.defaultAnalysis_3040   = process.CPDC3040.clone()
process.defaultAnalysis_4050   = process.CPDC4050.clone()
process.defaultAnalysis_5060   = process.CPDC5060.clone()
process.defaultAnalysis_6070   = process.CPDC6070.clone()
process.defaultAnalysis_7080   = process.CPDC7080.clone()

process.defaultAnalysis_1015   = process.CPDC1015.clone()
process.defaultAnalysis_1520   = process.CPDC1520.clone()
process.defaultAnalysis_2025   = process.CPDC2025.clone()
process.defaultAnalysis_2530   = process.CPDC2530.clone()

process.defaultAnalysis_3035   = process.CPDC3035.clone()
process.defaultAnalysis_3540   = process.CPDC3540.clone()
process.defaultAnalysis_4045   = process.CPDC4045.clone()
process.defaultAnalysis_4550   = process.CPDC4550.clone()

process.defaultAnalysis_5055   = process.CPDC5055.clone()
process.defaultAnalysis_5560   = process.CPDC5560.clone()
process.defaultAnalysis_6065   = process.CPDC6065.clone()
process.defaultAnalysis_6570   = process.CPDC6570.clone()

process.defaultAnalysis_7075   = process.CPDC7075.clone()
process.defaultAnalysis_7580   = process.CPDC7580.clone()
process.defaultAnalysis_8085   = process.CPDC8085.clone()
process.defaultAnalysis_8590   = process.CPDC8590.clone()



process.p = cms.Path(#process.generalAndHiPixelTracks * 
                     process.eventFilter_HM *
                     process.hltfilter *
                     process.centralityBin*
   		     process.defaultAnalysis_05 * 
                     process.defaultAnalysis_510 *
                     process.defaultAnalysis_1015 *
                     process.defaultAnalysis_1520 *
                     process.defaultAnalysis_2025 *
                     process.defaultAnalysis_2530 *
                     process.defaultAnalysis_3035 *
                     process.defaultAnalysis_3540 *
                     process.defaultAnalysis_4050 *
                     process.defaultAnalysis_5060 *
                     process.defaultAnalysis_6070
#                     process.generalAndHiPixelTracks *
                  #   process.centralityBin*
                     #process.V2 * process.V3 * process.V4 *
                     #process.V2_std *
    #process.V3_std
                     # Compute centrality
                     #process.SAYANCMW
   )
                     #process.defaultAnalysis_05 *#)
                     #process.defaultAnalysis_510 )#*
#                     process.defaultAnalysis_1020 *
#                     process.defaultAnalysis_2030 )
#                     process.defaultAnalysis_3040 )#*
#                     process.defaultAnalysis_4050 *#)
#                     process.defaultAnalysis_5060 *
#                     process.defaultAnalysis_6070 *
#                     process.defaultAnalysis_7080 )

#process.defaultAnalysis_1015 *                                                                                                                                                                         
#process.defaultAnalysis_1520 *                                                                                                                                                                         
#process.defaultAnalysis_2025 *                                                                                                                                                                         
#process.defaultAnalysis_2530 )#*                                                                                                                                                                       

#process.defaultAnalysis_3035 *                                                                                                                                                                         
#process.defaultAnalysis_3540 *                                                                                                                                                                         
#process.defaultAnalysis_4045 *                                                                                                                                                                         
#process.defaultAnalysis_4550 )                                                                                                                                                                         

#process.defaultAnalysis_5055 *                                                                                                                                                                         
#process.defaultAnalysis_5560 *                                                                                                                                                                         
#process.defaultAnalysis_6065 *                                                                                                                                                                         
#process.defaultAnalysis_6570 *                                                                                                                                                                         
#process.defaultAnalysis_7075 *                                                                                                                                                                         
#process.defaultAnalysis_7580 *                                                                                                                                                                         
#process.defaultAnalysis_8085 *                                                                                                                                                                         
#process.defaultAnalysis_8590 )         




#process.schedule = cms.Schedule(process.p)





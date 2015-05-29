# lumicalc

How to calculate luminosity information of a given trigger in a forest. 

Step 1: Setup the cms lumi scripts

```bash
# will probably work with many releasees, but let's use 5_3_20
cmsrel CMSSW_5_3_20
cd CMSSW_5_3_20/src
mkdir -p RecoLuminosity
curl https://codeload.github.com/cms-sw/RecoLuminosity-LumiDB/tar.gz/V04-02-10  | tar xzv -C RecoLuminosity
mv RecoLuminosity/RecoLuminosity-LumiDB-* RecoLuminosity/LumiDB
cd RecoLuminosity/LumiDB
scramv1 b
cmsenv
```

Step 2: get 


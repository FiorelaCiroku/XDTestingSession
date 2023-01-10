import json
import os
import re
import sys
from urllib import response
import requests as issue
from urllib.request import urlopen
import rdflib
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import FOAF
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from rdflib.namespace import DC
from rdflib.namespace import OWL
from rdflib.namespace import XSD
from pytablewriter import MarkdownTableWriter
from datetime import date

# Load data from a JSON file
def loadDataFromJsonFile(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Get the ontology name
def getOntologiesName(data):
    name = data.get("ontologies")[0]['name']
    # Removing space
    return name.replace(" ", "") 

# Create ontology directory
def createOntologiesDirectory(name):
    # Directory
    directory = name
    # Parent Directory path
    parent_dir = "./XDTesting"
    try:
        # Path
        path = os.path.join(parent_dir, directory)

        if not os.path.exists(path):
            os.makedirs(path)
            print("Directory '% s' created" % directory)

        if not os.path.exists(path + '/TestDocumentation'):
            os.mkdir(path + '/TestDocumentation')

        if not os.path.exists(path + '/CompetencyQuestionVerificationTest'):
            os.mkdir(path + '/CompetencyQuestionVerificationTest')

        if not os.path.exists(path + '/InferenceVerificationTest'):
            os.mkdir(path + '/InferenceVerificationTest')

        if not os.path.exists(path + '/ErrorProvocationTest'):
            os.mkdir(path + '/ErrorProvocationTest')

        if not os.path.exists(path + '/TestDocumentation/PassedTests'):
            os.mkdir(path + '/TestDocumentation/PassedTests')
            file = open(
                path + "/TestDocumentation/PassedTests/README.md", "w+")
            file.write("This directory stores successfully passed tests.")
            file.close()

        if not os.path.exists(path + '/TestDocumentation/FailedTests'):
            os.mkdir(path + '/TestDocumentation/FailedTests')

            file = open(
                path + "/TestDocumentation/FailedTests/README.md", "w+")
            file.write("This directory stores failed tests.")
            file.close()

        if not os.path.exists(path + '/CompetencyQuestionVerificationTest/CQTestCase'):
            os.mkdir(path + '/CompetencyQuestionVerificationTest/CQTestCase')
            file = open(
                path + "/CompetencyQuestionVerificationTest/CQTestCase/README.md", "w+")
            file.write(
                "This directory stores Competency Question Verification test cases.")
            file.close()

        if not os.path.exists(path + '/CompetencyQuestionVerificationTest/CQDataSet'):
            os.mkdir(path + '/CompetencyQuestionVerificationTest/CQDataSet')

            file = open(
                path + "/CompetencyQuestionVerificationTest/CQDataSet/README.md", "w+")
            file.write(
                "This directory stores the sample dataset for the Competency Question Verification test cases.")
            file.close()

        if not os.path.exists(path + '/InferenceVerificationTest/IVTestCase'):
            os.mkdir(path + '/InferenceVerificationTest/IVTestCase')
            file = open(
                path + "/InferenceVerificationTest/IVTestCase/README.md", "w+")
            file.write(
                "This directory stores Inference Verification test cases.")
            file.close()

        if not os.path.exists(path + '/InferenceVerificationTest/IVDataSet'):
            os.mkdir(path + '/InferenceVerificationTest/IVDataSet')

            file = open(
                path + "/InferenceVerificationTest/IVDataSet/README.md", "w+")
            file.write(
                "This directory stores the sample dataset for the Inference Verification test cases.")
            file.close()

        if not os.path.exists(path + '/ErrorProvocationTest/EPTestCase'):
            os.mkdir(path + '/ErrorProvocationTest/EPTestCase')
            file = open(
                path + "/ErrorProvocationTest/EPTestCase/README.md", "w+")
            file.write(
                "This directory stores Error Provocation test cases.")
            file.close()

        if not os.path.exists(path + '/ErrorProvocationTest/EPDataSet'):
            os.mkdir(path + '/ErrorProvocationTest/EPDataSet')

            file = open(
                path + "/ErrorProvocationTest/EPDataSet/README.md", "w+")
            file.write(
                "This directory stores the sample dataset for the Error Provocation test cases.")
            file.close()

    except OSError as error:
        print(error)

# Get fragment name
def getFragmentsName(data):
    listOfFragmentName = []
    for fragment in data['fragments']:
        fragmentDetail = []
        fragmentDetail.append(fragment['name'].replace(" ", ""))
        fragmentDetail.append(fragment.get('ontologyName').replace(" ", ""))
        listOfFragmentName.append(fragmentDetail)
    return listOfFragmentName

# Create fragment directory
def createFragmentDirectory(fragmentName, name):
    # Directory
    directory = fragmentName
    # Parent Directory path
    parent_dir = "./XDTesting/"+name
    # Path
    try:
        # Path
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.makedirs(path)
            file = open(
                path + "/README.md", "w+")
            file.write(
                "Fragment")
            file.close()
            # os.makedirs()
        if not os.path.exists(path + '/TestDocumentation'):
            os.mkdir(path + '/TestDocumentation')

        if not os.path.exists(path + '/CompetencyQuestionVerificationTest'):
            os.mkdir(path + '/CompetencyQuestionVerificationTest')

        if not os.path.exists(path + '/InferenceVerificationTest'):
            os.mkdir(path + '/InferenceVerificationTest')

        if not os.path.exists(path + '/ErrorProvocationTest'):
            os.mkdir(path + '/ErrorProvocationTest')

        if not os.path.exists(path + '/TestDocumentation/PassedTests'):
            os.mkdir(path + '/TestDocumentation/PassedTests')
            file = open(
                path + "/TestDocumentation/PassedTests/README.md", "w+")
            file.write("This directory stores successfully passed tests.")
            file.close()

        if not os.path.exists(path + '/TestDocumentation/FailedTests'):
            os.mkdir(path + '/TestDocumentation/FailedTests')

            file = open(
                path + "/TestDocumentation/FailedTests/README.md", "w+")
            file.write("This directory stores failed tests.")
            file.close()

        if not os.path.exists(path + '/CompetencyQuestionVerificationTest/CQTestCase'):
            os.mkdir(path + '/CompetencyQuestionVerificationTest/CQTestCase')
            file = open(
                path + "/CompetencyQuestionVerificationTest/CQTestCase/README.md", "w+")
            file.write(
                "# Competency Question Verification Test \n")
            file.write(
                "This directory stores Competency Question Verification test cases.\n")
            file.write(
                "Competency Question Verification tests allow to verify if the ontology can answer the competency questions that have been collected during the requirement collection.")
            file.close()

        if not os.path.exists(path + '/CompetencyQuestionVerificationTest/CQDataSet'):
            os.mkdir(path + '/CompetencyQuestionVerificationTest/CQDataSet')

            file = open(
                path + "/CompetencyQuestionVerificationTest/CQDataSet/README.md", "w+")
            file.write(
                "This directory stores the sample data for the Competency Question Verification test cases.")
            file.close()

        if not os.path.exists(path + '/InferenceVerificationTest/IVTestCase'):
            os.mkdir(path + '/InferenceVerificationTest/IVTestCase')
            file = open(
                path + "/InferenceVerificationTest/IVTestCase/README.md", "w+")
            file.write(
                "This directory stores Inference Verification test cases.")
            file.close()

        if not os.path.exists(path + '/InferenceVerificationTest/IVDataSet'):
            os.mkdir(path + '/InferenceVerificationTest/IVDataSet')

            file = open(
                path + "/InferenceVerificationTest/IVDataSet/README.md", "w+")
            file.write(
                "This directory stores the sample data for the Inference Verification test cases.")
            file.close()

        if not os.path.exists(path + '/ErrorProvocationTest/EPTestCase'):
            os.mkdir(path + '/ErrorProvocationTest/EPTestCase')
            file = open(
                path + "/ErrorProvocationTest/EPTestCase/README.md", "w+")
            file.write(
                "This directory stores Error Provocation test cases.")
            file.close()

        if not os.path.exists(path + '/ErrorProvocationTest/EPDataSet'):
            os.mkdir(path + '/ErrorProvocationTest/EPDataSet')

            file = open(
                path + "/ErrorProvocationTest/EPDataSet/README.md", "w+")
            file.write(
                "This directory stores the sample data for the Error Provocation test cases.")
            file.close()

        os.mkdir(path)

    except OSError as error:
        print(error)
    print("Directory '% s' created" % directory)

# Validate the expected result by loading JSON
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
        print("Success!")
    except ValueError as error:
        print("Error - "+error)

# Validate SPARQL by preparing query
def validateSPARQL(query):
    print("The variable is ", query)
    try:
        q = prepareQuery(query, initNs={
                         "foaf": FOAF, "rdfs": RDFS, "rdf": RDF, "owl": OWL, "xsd": XSD},)
        print("Success!")

    except Exception as error:
        print("Error - "+error)

# Get test type
def getTestType(test):
    return test.get('type')

# Get content (competency question)
def getContent(test):
    return test.get('content')

# Get query content
def getQueryContent(test):
    if test.get('query') is None:
        queryPath = '.xd-testing/' + test.get('queryFileName')
        file = open(queryPath, "r")
        return file.read()
    else:
        # return urlopen(test.get('query')).read()
        return test.get('query')

# Get expected result
def getExpectedResultsContent(test):
    if test.get('expectedResults') is None:
        testPath = '.xd-testing/' + test.get('expectedResultsFileName')
        file = open(testPath, "r")
        return file.read()
    else:
        return test.get('expectedResults')

# Get data
def getData(test):
    if test.get('data') is None:
        dataPath = '.xd-testing/' + test.get('dataFileName')
        file = open(dataPath, "r")
        return file.read()
    else:
        return test.get('data')

# Get test ID
def getID(test):
    return test.get('id')

# Get reasoner
def getReasoner(test):
    return test.get('reasoner')

# Get ontology url
def getOntologyUrl(test):
    return test.get("ontologies")[0]['url']
     

# Update test status
def setCheckValue(filename, value, indexFragment, indexTest):
    data = loadDataFromJsonFile(filename)
    data['fragments'][indexFragment]['tests'][indexTest]['check'] = value
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                  indent=4,
                  separators=(',', ': '))
        json_file.close()

# Get check value
def getCheckValue(data, indexFragment, indexTest):
    try:
        return data['fragments'][indexFragment]['tests'][indexTest]['check']
    except:
        return None

# Set status value
def setStatusValue(filename, value, indexFragment, indexTest):
    data = loadDataFromJsonFile(filename)
    data['fragments'][indexFragment]['tests'][indexTest]['status'] = value
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                  indent=4,
                  separators=(',', ': '))
        json_file.close()

# Set status notes
def setStatusNotesValue(filename, value, indexFragment, indexTest):
    data = loadDataFromJsonFile(filename)
    data['fragments'][indexFragment]['tests'][indexTest]['statusNotes'] = str(
        value)
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                  indent=4,
                  separators=(',', ': '))
        json_file.close()

# Create test case and data set file
def createTestCaseAndDataSetFile(fileData, fileName, repoName):
    for indexFragment in range(len(fileData['fragments'])):
        for indexTest in range(len(fileData['fragments'][indexFragment]['tests'])):
            if (getCheckValue(fileData, indexFragment, indexTest) is None or getCheckValue(fileData, indexFragment, indexTest) == 0):
                testData = fileData['fragments'][indexFragment]['tests'][indexTest]
                print(testData)
                if (getTestType(testData) == 'COMPETENCY_QUESTION'):
                    try:
                        # validateSPARQL(getQueryContent(testData))
                        # validateJSON(getExpectedResultsContent(testData))

                        testFileLink = "https://raw.githubusercontent.com/"+repoName+"/main/XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/CompetencyQuestionVerificationTest/"

                        testFilePath = "./XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/CompetencyQuestionVerificationTest/"
                        with open(testFilePath+'/CQTestCase/'+getID(testData)+'.ttl', 'w') as f:
                            f.write(
                                '@prefix owlunit: <https://w3id.org/OWLunit/ontology/> .\n')
                            f.write(
                                '@prefix ns: <'+ 'https://raw.githubusercontent.com/'+repoName+'/main/.xd-testing/' + fileData['fragments'][indexFragment]['fileName'] + '> .\n')
                            f.write('@prefix td: <' +
                                    testFileLink+'CQDataSet/> .\n')
                            f.write('@prefix tc: <'+testFileLink +
                                    'CQTestCase/> .\n\n')
                            f.write('tc:'+getID(testData) +
                                    ' a owlunit:CompetencyQuestionVerification ;\n')
                            f.write('\towlunit:hasCompetencyQuestion \"' +
                                    getContent(testData)+'\" ;\n')
                            f.write('\towlunit:hasSPARQLUnitTest \"' +
                                    getQueryContent(testData)+'\" ;\n')
                            f.write('\towlunit:hasInputData td:' +
                                    getID(testData)+'TD.ttl ;\n')
                            f.write(
                                '\towlunit:hasInputTestDataCategory owlunit:ToyDataset ;\n')
                            f.write(
                                '\towlunit:hasExpectedResult \"'+getExpectedResultsContent(testData)+'\" ;\n')
                            f.write(
                                '\towlunit:testsOntology ns: .\n')
                            print(f.read())
                            f.close()

                        with open(testFilePath+'/CQDataSet/'+getID(testData)+'TD.ttl', 'w') as f:
                            f.write(
                                getData(testData))
                            f.close()
                    except Exception as error:
                        setStatusValue(fileName, 'warning',
                                       indexFragment, indexTest)
                        setStatusNotesValue(fileName, error,
                                            indexFragment, indexTest)

                elif (getTestType(testData) == 'INFERENCE_VERIFICATION'):
                    try:
                        # validateSPARQL(getQueryContent(testData))
                        testFileLink = "https://raw.githubusercontent.com/"+repoName+"/main/XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/InferenceVerificationTest/"

                        testFilePath = "./XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/InferenceVerificationTest/"
                        with open(testFilePath+'/IVTestCase/'+getID(testData)+'.ttl', 'w') as f:
                            f.write(
                                '@prefix owlunit: <https://w3id.org/OWLunit/ontology/> .\n')
                            f.write(
                                '@prefix ns: <'+ 'https://raw.githubusercontent.com/'+repoName+'/main/.xd-testing/' + fileData['fragments'][indexFragment]['fileName'] + '> .\n')
                            f.write('@prefix td: <' +
                                    testFileLink+'IVDataSet/> .\n')
                            f.write('@prefix tc: <'+testFileLink +
                                    'IVTestCase/> .\n\n')
                            f.write('tc:'+getID(testData) +
                                    ' a owlunit:InferenceVerificationTest ;\n')
                            f.write('\towlunit:hasCompetencyQuestion \"' +
                                    getContent(testData)+'\" ;\n')
                            f.write('\towlunit:hasSPARQLUnitTest \"' +
                                    getQueryContent(testData)+'\" ;\n')
                            f.write('\towlunit:hasInputData td:' +
                                    getID(testData)+'TD.ttl ;\n')
                            f.write(
                                '\towlunit:hasInputTestDataCategory owlunit:ToyDataset ;\n')
                            f.write(
                                '\towlunit:hasExpectedResult true ;\n')
                            f.write(
                                '\towlunit:hasReasoner owlunit:'+getReasoner(testData)+' ;\n')
                            f.write(
                                '\towlunit:testsOntology ns: .\n')
                            f.close()
                        with open(testFilePath+'/CQDataSet/'+getID(testData)+'TD.ttl', 'w') as f:
                            f.write(
                                getData(testData))
                            f.close()
                    except Exception as error:
                        setStatusValue(fileName, 'warning',
                                       indexFragment, indexTest)
                        setStatusNotesValue(fileName, error,
                                            indexFragment, indexTest)

                elif (getTestType(testData) == 'ERROR_PROVOCATION'):

                    print("ID : "+getID(testData))
                    print("Data : "+getData(testData))
                    try:
                        testFileLink = "https://raw.githubusercontent.com/"+repoName+"/main/XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/ErrorProvocation/"

                        testFilePath = "./XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/ErrorProvocation/"
                        with open(testFilePath+'/IVTestCase/'+getID(testData)+'.ttl', 'w') as f:
                            f.write(
                                '@prefix owlunit: <https://w3id.org/OWLunit/ontology/> \n')
                            f.write(
                                '@prefix ns: <'+ 'https://raw.githubusercontent.com/'+repoName+'/main/.xd-testing/' + fileData['fragments'][indexFragment]['fileName'] + '> .\n')
                            f.write('@prefix td: <' +
                                    testFileLink+'EPDataSet/> .\n')
                            f.write('@prefix tc: <'+testFileLink +
                                    'EPTestCase/> .\n\n')
                            f.write('tc:'+getID(testData) +
                                    ' a owlunit:ErrorProvocation ;\n')
                            f.write('\towlunit:hasInputData td:' +
                                    getID(testData)+'TD.ttl ;\n')
                            f.write(
                                '\towlunit:testsOntology ns: .\n')
                            f.close()
                        with open(testFilePath+'/CQDataSet/'+getID(testData)+'TD.ttl', 'w') as f:
                            f.write(
                                getData(testData))
                            fileContent = f.read()
                            print(fileContent)
                            f.close()
                    except Exception as error:
                        setStatusValue(fileName, 'warning',
                                       indexFragment, indexTest)
                        setStatusNotesValue(fileName, error,
                                            indexFragment, indexTest)

            else:
                print('Test Case and Data Set already Created ')


def createTestDocumentation(testFilePath, result, testData, folderName, error="Error"):
    print(testData)
    if result == "PASSED":
        writer = MarkdownTableWriter(
            headers=["Test case documentation",
                     "Information"],
            value_matrix=[
                ["Test case ID", getID(testData)],
                ["Test category", getTestType(testData)],
                ["Requirement",   getContent(testData)],
                ["Test", getQueryContent(testData)],
                ["Input test data", str(folderName) +
                 str(getID(testData))+'TD.ttl'],
                ["Expected result", getExpectedResultsContent(testData)],
                ["Actual result", getExpectedResultsContent(testData)],
                ["Executed on", date.today()],
                ["Environment", "GITHUB"],
                ["Execution result", result],
                ["Execution comment", ""],

            ],
            margin=1  # add a whitespace for both sides of each cell
        )
        writer.dump(str(testFilePath)+'PassedTests/' +
                    str(getID(testData))+'.md')
    elif result == "FAILED":
        writer = MarkdownTableWriter(
            headers=["Test case documentation",
                     "v1"],
            value_matrix=[
                ["Test case ID", getID(testData)],
                ["Test category", getTestType(testData)],
                ["Requirement",   getContent(testData)],
                ["Test", getQueryContent(testData)],
                ["Input test data", str(folderName) +
                 str(getID(testData))+'TD.ttl'],
                ["Expected result", getExpectedResultsContent(testData)],
                ["Actual result", str(error)],
                ["Executed on", date.today()],
                ["Environment", "GITHUB"],
                ["Execution result", result],
                ["Execution comment", ""],

            ],
            margin=1  # add a whitespace for both sides of each cell
        )
        writer.dump(str(testFilePath)+'FailedTests/' +
                    str(getID(testData))+'.md')


def executeTestCase(fileData, fileName, repoName, token):
    headers = {"Authorization": "token {}".format(token)}
    url = "https://api.github.com/repos/{}/issues".format(
        repoName)

    for indexFragment in range(len(fileData['fragments'])):
        for indexTest in range(len(fileData['fragments'][indexFragment]['tests'])):
            if (getCheckValue(fileData, indexFragment, indexTest) is None or getCheckValue(fileData, indexFragment, indexTest) == 0):
                testData = fileData['fragments'][indexFragment]['tests'][indexTest]
                if (getTestType(testData) == 'COMPETENCY_QUESTION'):
                    try:
                        testFileLink = "https://raw.githubusercontent.com/"+repoName+"/main/XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/CompetencyQuestionVerificationTest/"

                        testFilePath = "./XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/TestDocumentation/"
                        print('---- Executing Test ----')
                        os.system(
                            "java -jar OWLUnit-0.3.2.jar --test-case "+testFileLink+"CQTestCase/"+getID(fileData)+".ttl")
                        print('---- PASSED ----')
                        createTestDocumentation(
                            testFilePath, "PASSED", testData, "CQDataSet/")
                        setCheckValue(fileName, 1,
                                      indexFragment, indexTest)
                    except Exception as error:
                        print('---- FAILED----')

                        data = {"title": getID(fileData), "body": error}
                        try:
                            createTestDocumentation(
                                testFilePath, "FAILED", testData, "CQDataSet/", error)
                            response = issue.post(url, data, headers=headers)
                            print(response)
                            setCheckValue(
                                fileName, 0, indexFragment, indexTest)
                        except Exception as error:
                            print("Error : "+error)

                elif (getTestType(testData) == 'INFERENCE_VERIFICATION'):
                    try:
                        testFileLink = "https://raw.githubusercontent.com/"+repoName+"/main/XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/InferenceVerificationTest/"

                        testFilePath = "./XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/TestDocumentation/"
                        print('---- Executing Test ----')
                        os.system(
                            "java -jar OWLUnit-0.3.2.jar --test-case "+testFileLink+"IVTestCase/"+getID(fileData)+".ttl")
                        print('---- PASSED ----')
                        createTestDocumentation(
                            testFilePath, "PASSED", testData, "IVDataSet/")
                        setCheckValue(fileName, 1,
                                      indexFragment, indexTest)
                    except Exception as error:
                        print('---- FAILED----')
                        data = {"title": getID(fileData), "body": error}
                        try:
                            createTestDocumentation(
                                testFilePath, "FAILED", testData, "IVDataSet/",  error)
                            response = issue.post(url, data, headers=headers)
                            print(response)
                            setCheckValue(
                                fileName, 0, indexFragment, indexTest)
                        except Exception as error:
                            print("Error : "+error)

                elif (getTestType(testData) == 'ERROR_PROVOCATION'):

                    print("ID : "+getID(testData))
                    print("Data : "+getData(testData))
                    try:
                        testFileLink = "https://raw.githubusercontent.com/"+repoName+"/main/XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/ErrorProvocation/"

                        testFilePath = "./XDTesting/" + fileData['fragments'][indexFragment]['ontologyName'].replace(
                            " ", "") + "/"+fileData['fragments'][indexFragment]['name'].replace(" ", "")+"/TestDocumentation/"
                        print("testFileLink" , testFileLink)
                        print("testFilePath", testFilePath)

                        print('---- Executing Test ----')
                        os.system(
                            "java -jar OWLUnit-0.3.2.jar --test-case "+testFileLink+"EPTestCase/"+getID(fileData)+".ttl")
                        print('---- PASSED ----')
                        createTestDocumentation(
                            testFilePath, "PASSED", testData, "EPDataSet/")
                        setCheckValue(fileName, 1,
                                      indexFragment, indexTest)
                    except Exception as error:
                        print('---- FAILED----')

                        data = {"title": getID(fileData), "body": error}
                        try:
                            createTestDocumentation(
                                testFilePath, "FAILED", testData, "EPDataSet/", error)
                            response = issue.post(url, data, headers=headers)
                            print(response)
                            setCheckValue(
                                fileName, 0, indexFragment, indexTest)
                        except Exception as error:
                            print("Error : "+error)

            else:
                print('Test already Executed')


# ---------------- Start---------------#
repoName = sys.argv[1]
arg = sys.argv[2]
token = sys.argv[3]

fileName = '.xd-testing/UserInput.json'
fileData = loadDataFromJsonFile(fileName)

if arg == "create":
    # Step 1 - Get ontology name
    ontologyName = getOntologiesName(fileData)

    # Step 2 - Create the GitHub directories for the ontology
    createOntologiesDirectory(ontologyName)

    # Step 3 - Get fragment name
    listOfFragmentName = getFragmentsName(fileData)
    print(listOfFragmentName)

    # Step 4 - Create the GitHub directories for the module
    for fragment, ontology in listOfFragmentName:
        createFragmentDirectory(fragment, ontology)

    # Step 5 - Create test cases and dataset files
    createTestCaseAndDataSetFile(fileData, fileName, repoName)

elif arg == "test":
    # Step 6 - Execute test cases
    executeTestCase(fileData, fileName, repoName, token)



# def getCountOfResults(squirrel):
#
#     resCount = None;
#
#     resElements = squirrel.find_XPATH("//h2[@class='pb2 t-black--light t-14']")
#
#     if resElements != None:
#         resInner = resElements.text
#         splitInner = resInner.split(" ")
#         if len(splitInner) == 3:
#             resCount = int(splitInner[1].replace(",",""))
#         elif len(splitInner) == 2:
#             resCount = int(splitInner[0].replace(",", ""))
#     else:
#         resCount = None
#
#     return resCount;

def getListOfCompany(squirrel):

    resultData = [];

    organizationList = squirrel.finds_XPATH("//tbody/tr")

    for elOrganization in organizationList:
        found = elOrganization.find_XPATH("./td/a")

        href = found.get_attribute('href')
        name = found.text

        reviewData = {}
        reviewData["href"] = href
        reviewData["name"] = name

        resultData.append(reviewData);

    return resultData;

# def getNumberCurentPaginationPage(squirrel):
#     result = None;
#
#     paginationSection = squirrel.find_XPATH('//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
#     if paginationSection != None:
#         curPagPageEl = paginationSection.find_XPATH('./li[@class="artdeco-pagination__indicator artdeco-pagination__indicator--number active selected ember-view"]')
#         if curPagPageEl != None:
#             try:
#                 result = int(curPagPageEl.get_attribute('data-test-pagination-page-btn'))
#             except Exception as e:
#                 result = None;
#
#     return result
#
# def getNumberLastPaginationPage(squirrel):
#     result = None;
#
#     paginationSection = squirrel.find_XPATH('//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
#     if paginationSection != None:
#         allPaginationButton = paginationSection.finds_XPATH('./li[@class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view"]')
#
#         for curPagDome in allPaginationButton:
#             try:
#                 result = int(curPagDome.get_attribute('data-test-pagination-page-btn'))
#             except Exception as e:
#                 pass
#
#     return result
#
# def getNextPaginationButton(squirrel):
#     result = squirrel.find_XPATH('//button[@aria-label="Next"]')
#     return result
#
# def pushNextPaginationButton(squirrel):
#     result = None
#
#     NextButton = getNextPaginationButton(squirrel);
#     if NextButton != None:
#         NextButton.click()
#         result = True
#
#     return result;
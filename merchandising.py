#!/usr/bin/env python3
from ebaysdk.merchandising import Connection

if __name__ == '__main__':
    api = Connection(config_file='ebay.yaml')
    results = api.execute('getCategorySpecifics', {})

for item in results.reply.itemRecommendations.item:
    print(
        f"The item {item.title} has been watched {item.watchCount} times")


'''
    <?xml version="1.0" encoding="utf-8"?>
<GetCategorySpecificsRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <!-- Call-specific Input Fields -->
  <CategoryID> string </CategoryID>
  <!-- ... more CategoryID values allowed here ... -->
  <CategorySpecific> CategoryItemSpecificsType
    <CategoryID> string </CategoryID>
    <!-- ... more CategoryID values allowed here ... -->
    <ItemSpecifics> NameValueListArrayType
      <NameValueList> NameValueListType
        <Name> string </Name>
        <Value> string </Value>
        <!-- ... more Value values allowed here ... -->
      </NameValueList>
      <!-- ... more NameValueList nodes allowed here ... -->
    </ItemSpecifics>
  </CategorySpecific>
  <!-- ... more CategorySpecific nodes allowed here ... -->
  <CategorySpecificsFileInfo> boolean </CategorySpecificsFileInfo>
  <ExcludeRelationships> boolean </ExcludeRelationships>
  <IncludeConfidence> boolean </IncludeConfidence>
  <LastUpdateTime> dateTime </LastUpdateTime>
  <MaxNames> int </MaxNames>
  <MaxValuesPerName> int </MaxValuesPerName>
  <Name> string </Name>
  <!-- Standard Input Fields -->
  <ErrorLanguage> string </ErrorLanguage>
  <MessageID> string </MessageID>
  <Version> string </Version>
  <WarningLevel> WarningLevelCodeType </WarningLevel>
</GetCategorySpecificsRequest>
'''

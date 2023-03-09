import json

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

app_secret = 'd4fc777f77ecc1fed686784ec855c42e'
app_id = '603141541175725'


def getCampaigns(request, User):
    try:
        FacebookAdsApi.init(access_token= (User.objects.first()).access_token)
        fields = [
            'name',
            'objective',
        ]
        params = {
            'effective_status': ['ACTIVE','PAUSED'],
        }
        campaigns = (AdAccount("act_" + (User.objects.first()).adsid).get_campaigns(fields=fields, params=params))

        return {"user" : User.objects.first(), "campaigns" : campaigns}

    except:
        return None
    
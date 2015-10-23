from ferrisnose import EndpointsTest
from app.lots import lot_service


class LotTest(EndpointsTest):

    def test_api(self):
        self.login("test@example.com")
        self.add_service(lot_service.LotService)
        
        #insert test
        params = {"location":{"lat":14,"lon":121},
                  "address":"Makati City",
                  "sale_price":1212,
                  "type":"industrial"
        }

        resp = self.invoke('LotService.insert', params)
        assert resp['address'] == 'Makati City'
        assert resp['type'] == 'industrial'

        
        #assert resp['author']['email'] == 'test@example.com'

        #list test
        # resp = self.invoke('LotService.list')

        # assert len(resp['items']) == 1
        # assert resp['items'][0]['address'] == 'Makati City'

        # #get Test
        # get_resp = self.invoke('LotsService.get', {'itemId': resp['items'][0]['id']})

        # assert get_resp['address'] == 'Makati City'
        
        #update Test
        # itemId = get_resp['id']
        # params = {
        #     'itemId': itemId,
        #     "address": "Manila City",
        #     "area": 1212,
        #     "sale_price": 1000,
        #     "type": "agriculture"
        # }

        # resp = self.invoke('LotsService.update', params)
        # assert resp['address'] == 'Manila City'
        # assert resp['type'] == 'agriculture'

        # assert 12==13
        

    def test_list(self):
        self.login("test@example.com")
        self.add_service(lot_service.LotService)

        params = {"location":{"lat":14,"lon":121},
                  "address":"Makati City",
                  "sale_price":1212,
                  "type":"industrial"
        }

        resp = self.invoke('LotService.insert', params)


        resp = self.invoke('LotService.list')

        assert len(resp['items']) == 1
        assert resp['items'][0]['address'] == 'Makati City'
        
        # #insert test
        # params = {"location":{"lat":14,"lon":121},
        #           "address":"Manila City",
        #           "sale_price":1212,
        #           "type":"agriculture"
        # }

        # resp = self.invoke('LotsService.insert', params)

        # assert resp['content'] == 'Makati City'
        # assert resp['type'] == 'industrial'
        # #assert resp['author']['email'] == 'test@example.com'


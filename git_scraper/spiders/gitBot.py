import scrapy

class userDetails(scrapy.Item):
	followers = scrapy.Field()
	starred = scrapy.Field()
	following = scrapy.Field()
	
	
	
class gitBot(scrapy.Spider):
	name = "gitBot"
	allowed_domains = ["github.com"]
	
	print "Enter your username, exactly as it is on https://github.com."
	user_name = raw_input('>')
	start_urls = ["https://github.com/"+user_name]
	
	
	
	
	def parse(self, response):
		
		people = response.xpath('//strong/text()').extract()
		
		print "You have a total of " + people[0] + " followers."
		print "You have a total of " + people[1] + " starred projects."
		print "You have a total of " + people[2] + " people following you."
		
		
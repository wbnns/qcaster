require 'qcaster/version'
require 'dotenv'
require 'rest-client'
require 'rufus-scheduler'

Dotenv.load

class QCaster

  WARP_API = "https://api.warpcast.com/v2/casts".freeze

  def initialize
    @scheduler = Rufus::Scheduler.new
  end

  def post_cast(cast_message)
    RestClient.post(
      WARP_API,
      { cast: cast_message },
      { Authorization: ENV['AUTHORIZATION_HEADER'] }
    )
  end

  def schedule_posts_from_file(file_name)
    File.foreach(file_name) do |cast_message|
      @scheduler.in '72m' do
        post_cast(cast_message.chomp)
      end
    end
  end

  def schedule_greetings
    @scheduler.cron '30 9 * * *' do
      post_cast('Gm')
    end
    @scheduler.cron '0 0 * * *' do
      post_cast('Gn')
    end
  end

  def start
    schedule_posts_from_file('casts.txt')
    schedule_greetings
    @scheduler.join
  end
end


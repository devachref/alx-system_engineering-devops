#!/usr/bin/env ruby

def match_school(input)
    regex = /hbtttn(t*)$/

    match_result = input.match(regex)

    puts match_result ? match_result[0] : ''
end

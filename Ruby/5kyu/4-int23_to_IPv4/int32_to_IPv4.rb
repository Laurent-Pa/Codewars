def int32_to_ip(int32)

string_bytes = int32.to_s(2)
nbr_missing_digits = 32 - string_bytes.length
full_string_bytes = ("0" * nbr_missing_digits).insert(nbr_missing_digits, string_bytes)

fourth_byte = full_string_bytes.slice!(24..31).to_i(2)
third_byte = full_string_bytes.slice!(16..23).to_i(2)
second_byte = full_string_bytes.slice!(8..15).to_i(2)
first_byte = full_string_bytes.slice!(0..7).to_i(2)
ip = "#{first_byte}.#{second_byte}.#{third_byte}.#{fourth_byte}"

# résolution en une seule ligne:
[24, 16, 8, 0].collect {|b| (int32 >> b) & 255}.join('.')
end

puts int32_to_ip(2149583361) == "128.32.10.1"
puts int32_to_ip(0) == "0.0.0.0"
puts int32_to_ip(185) == "0.0.0.185"

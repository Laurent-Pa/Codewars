def rgb(r, g, b)
  hex_code = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

  dig_code = [r, g, b]
  hex_color =""
  dig_code.each do |color|
    if color < 0
      hex_color << "00"
    elsif color > 255
      hex_color << "FF"
    else
      first_digit = color / 16
      second_digit = color % 16
      hex_color << hex_code[first_digit] + hex_code[second_digit]
    end
  end

  return hex_color

  # One line solution:
  # "%.2X%.2X%.2X" % [r,g,b].map{|i| [[i,255].min,0].max}
end

# composition du code hexadecimal
# RRGGBB

# 00 = 0 en décimal
# FF = 255 en décimal
# codage systeme hexadecimal: [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]

puts "Résultat #{rgb(148,0,211)}"
# gérer le cas d'un nombre négatif
puts "Résultat #{rgb(0, 0, -20)}"
# gérer le cas d'un nombre supérieur à 255
puts "Résultat #{rgb(300,255,255)}"

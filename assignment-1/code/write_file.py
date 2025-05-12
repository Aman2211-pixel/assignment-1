# Open a file in write mode (it will create the file if it doesn't exist)
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, this is a sample text file.\n")
file.write("You can write multiple lines like this.\n")
file.write("Python makes file handling easy!")

# Close the file
file.close()

print("Content written to 'example.txt'")

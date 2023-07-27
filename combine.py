def combine(image_url, text_input): 
    import requests
    from PIL import Image, ImageDraw, ImageFont
    import textwrap

    def add_multiline_text(image_path, text, font_path, line_spacing):
        # Open the image
        image = Image.open(image_path)
        width, height = image.size

        # Create a transparent text layer
        text_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)

        # Calculate the text size and position
        max_width = width * 0.8  # Adjust the width percentage as desired
        max_height = height * 0.8  # Adjust the height percentage as desired
        font_size = 48  # Initial font size
        font = ImageFont.truetype(font_path, font_size)

        # Wrap the text into multiple lines
        lines = textwrap.wrap(text, width=int(2*max_width / font_size))

        # Calculate the line heights
        line_heights = [draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines]

        # Adjust the font size to fit within the maximum width and height
        while True:
            # Calculate the text bounding box
            text_bbox = draw.textbbox((0, 0), lines[0], font=font)

            # Calculate the total text size
            text_width = text_bbox[2] - text_bbox[0]
            text_height = sum(line_heights) + line_spacing * (len(lines) - 1)

            if text_width <= max_width and text_height <= max_height:
                break

            font_size -= 2
            font = ImageFont.truetype(font_path, font_size)

            line_heights = [draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines]

        x = (width - text_width) // 2
        y = (height - text_height) // 2

        # Draw multiline text
        for line, line_height in zip(lines, line_heights):
            line_bbox = draw.textbbox((0, 0), line, font=font)
            line_width = line_bbox[2] - line_bbox[0]
            draw.text((x + (text_width - line_width) // 2, y), line, font=font, fill=(255, 255, 255, 255))
            y += line_height + line_spacing

        # Composite the image and the text layer
        result = Image.alpha_composite(image.convert('RGBA'), text_layer)

        # Save the modified image
        result.save('C:\MEGA\Projects\Django\AutoPoster\modified_image.png')

    # Example usage
    font_path = "C:\MEGA\Projects\Django\AutoPoster\Roboto-Regular.ttf"
    line_spacing = 50  # Adjust the line spacing value as desired

    # Download the image
    response = requests.get(image_url)
    image_path = 'C:\MEGA\Projects\Django\AutoPoster\image.jpg'
    with open(image_path, 'wb') as f:
        f.write(response.content)
    from PIL import Image

    def apply_transparent_mask(image_path, output_path):
        # Open the image
        image = Image.open(image_path)

        # Create a new image with the same dimensions and mode as the original image
        mask = Image.new("RGBA", image.size, (0, 0, 0, 128))

        # Apply the mask to the original image
        masked_image = Image.alpha_composite(image.convert("RGBA"), mask)

        # Save the result
        masked_image.save(output_path, 'PNG')

    # Specify the paths to the input image and the desired output
    apply_transparent_mask(image_path, image_path)
    # Add text to the image
    add_multiline_text(image_path, text_input, font_path, line_spacing)

    print("Image with text added: modified_image.png")

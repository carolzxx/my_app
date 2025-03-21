import gradio as gr

# Placeholder function (no AI model yet)
def dummy_recipe(image):
    """Placeholder function to simulate food recognition and recipe generation."""
    return "Predicted Dish: 🍕 Pizza", "Ingredients:\n- 2 cups flour\n- 1/2 cup tomato sauce\n- 1 cup mozzarella", "Steps:\n1. Mix flour and yeast\n2. Knead dough\n3. Add toppings\n4. Bake at 220°C"

# Gradio App Layout
with gr.Blocks() as demo:
    gr.Markdown("# 🍽️ DishVision AI - Identify Your Dish & Get Recipes")
    gr.Markdown("Upload a picture of a dish, and get its name, ingredients, and cooking instructions.")

    with gr.Row():
        image_input = gr.Image(label="Upload a Food Image", type="filepath")
    
    submit_button = gr.Button("Recognize Dish")

    with gr.Row():
        dish_name = gr.Textbox(label="Predicted Dish", interactive=False)

    with gr.Row():
        ingredients = gr.Textbox(label="Ingredients", interactive=False, lines=5)
        steps = gr.Textbox(label="Cooking Steps", interactive=False, lines=5)

    submit_button.click(dummy_recipe, inputs=image_input, outputs=[dish_name, ingredients, steps])

if __name__ == "__main__":
    demo.launch()

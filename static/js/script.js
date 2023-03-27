$(document).ready(function(){
    $(".delete").click(function(){
        return confirm('Are you sure you want to delete this category? All posts in this category will be deleted. This action cannot be undone')
    })
})
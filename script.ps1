# Define the root directory for the project
$rootDir = "src"

# Define the directory and file structure
$structure = @{
    "main.py" = $null
    "config.py" = $null
    "assets" = @{
        "images" = $null
        "sounds" = $null
        "fonts" = $null
    }
    "core" = @{
        "game.py" = $null
        "scene_manager.py" = $null
        "input_handler.py" = $null
    }
    "scenes" = @{
        "menu_scene.py" = $null
        "game_scene.py" = $null
        "pause_scene.py" = $null
    }
    "entities" = @{
        "entity.py" = $null
        "player.py" = $null
        "enemy.py" = $null
        "bomb.py" = $null
        "explosion.py" = $null
    }
    "ai" = @{
        "behavior_tree" = @{
            "enemies_behavior.py" = $null
        }
        "pathfinding" = @{
            "astar.py" = $null
            "grid.py" = $null
        }
    }
    "map" = @{
        "tile.py" = $null
        "level.py" = $null
        "level_loader.py" = $null
    }
    "utils" = @{
        "sprite_loader.py" = $null
        "collision.py" = $null
    }
}

# Function to create directories and files recursively
function Create-Structure {
    param (
        [string]$basePath,
        [hashtable]$structure
    )

    foreach ($key in $structure.Keys) {
        $currentPath = Join-Path -Path $basePath -ChildPath $key

        if ($structure[$key] -eq $null) {
            # If the value is null, create a file
            New-Item -Path $currentPath -ItemType File -Force
        } else {
            # If the value is a hashtable, create a directory
            New-Item -Path $currentPath -ItemType Directory -Force
            Create-Structure -basePath $currentPath -structure $structure[$key]
        }
    }
}

# Create the root directory
New-Item -Path $rootDir -ItemType Directory -Force

# Create the project structure
Create-Structure -basePath $rootDir -structure $structure

Write-Host "Project structure created successfully!"